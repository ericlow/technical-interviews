# E-Commerce Platform — Solution

## Approach

Standard microservices behind an API gateway, with an event bus for async work.
The core insight the interviewer was probing: security is layered (gateway
authenticates, services authorize), notifications are decoupled via events, and
the order write path stays fast by pushing everything non-essential off the
request thread. Answer the follow-ups with concrete mechanics, not diagrams.

## High-Level Architecture

```
Client (React SPA)
   │  HTTPS
   ▼
CDN / WAF ──► API Gateway ──► [auth: validate JWT, rate limit, route]
                               │
        ┌──────────────┬───────┴────────┬───────────────┐
        ▼              ▼                ▼               ▼
   User/Auth svc   Catalog svc    Order svc        Payment svc
        │              │                │               │
        └──────────────┴────────┬───────┴───────────────┘
                                 ▼
                      Event bus (Kafka / SNS+SQS)
                                 │
                    ┌────────────┴────────────┐
                    ▼                          ▼
             Notification svc           Analytics / audit
```

- **Data:** each service owns its DB (Postgres for orders/users, read replicas
  for catalog; Redis for sessions/cart/hot catalog cache).
- **Scale to 100k concurrent:** stateless services behind a load balancer,
  horizontal autoscaling, CDN for static assets and product images, caching
  layer (Redis) in front of read-heavy catalog, DB read replicas, and async
  offload of anything not needed to return the response.

## Security / Auth (the deep-dive)

**How does security work? JWT?** Yes. Flow:

1. User authenticates against the Auth service → receives a short-lived JWT
   access token + a long-lived refresh token (refresh stored httpOnly).
2. Client sends `Authorization: Bearer <jwt>` on every request.
3. The **API gateway validates the JWT** — signature, `exp`, `iss`, `aud` —
   and rejects unauthenticated requests before they ever reach a service.

**Details of the JWT:**
- Three parts: header (`alg`, `typ`), payload (claims), signature.
- Claims: `sub` (user id), `iss`, `aud`, `exp`, `iat`, plus `roles`/`scopes`.
- **Signing:** prefer asymmetric **RS256** — Auth service signs with a private
  key, gateway/services verify with the public key (fetched via JWKS endpoint,
  cached, rotated by `kid`). Symmetric HS256 would force sharing a secret across
  services, so avoid it.
- Keep tokens short-lived (~15 min) so revocation lag is small; use refresh
  tokens for renewal. For hard revocation, keep a small denylist (by `jti`) in
  Redis.

**Gateway → microservice, what happens with security?**
- The gateway sits at the trust boundary and does the expensive validation once.
- It forwards the request inside the trust zone. Two common patterns:
  - **Pass the JWT through** — each service re-verifies the signature (public
    key, cheap) and reads claims locally. No per-request call back to Auth.
  - Or the gateway swaps the external token for an **internal signed token /
    injects identity headers** (`X-User-Id`, `X-Roles`) over mTLS.
- Service-to-service calls use **mTLS** (or a service mesh like Istio) so
  internal traffic is authenticated too — don't assume the network is safe.

**Roles & permissions — are there lookups?**
- **RBAC:** users → roles → permissions.
- Coarse roles (`customer`, `admin`, `warehouse`) fit in the JWT claims, so the
  common case needs **no lookup** — the service authorizes from claims.
- Fine-grained or frequently-changing permissions shouldn't bloat the token:
  put a stable `role` in the JWT and resolve role→permissions from a cached
  lookup (Redis, backed by the Auth DB) at the service. Trade-off: claims in the
  token are fast but stale until the token expires; lookups are fresh but add a
  hop.
- Enforce at two layers: gateway does coarse route-level checks; each service
  does the authoritative resource-level check (e.g. "can this user view *this*
  order?").

## Order Creation API

`POST /orders` end-to-end:

1. **Validate** — auth/permission check, then payload validation: items exist,
   quantities > 0, price integrity, address valid. Reject fast (400) on bad
   input.
2. **Reserve / check inventory** — synchronous check against inventory service
   (or reserve stock) so you don't accept an unfulfillable order.
3. **Persist** — write the order in `PENDING` state in a single DB transaction.
   Use an **idempotency key** (client-supplied) to make retries safe and avoid
   duplicate orders.
4. **Payment** — either synchronous authorize, or emit an event and move through
   a saga; on success transition `PENDING → CONFIRMED`.
5. **Notify asynchronously** — publish an `OrderStatusChanged` event to the bus.
   The Notification service consumes it and sends email/SMS/push. This is the
   "async notifications on order-status change" requirement: the order response
   returns immediately; notification happens off the request thread.
6. **Respond** — return the order id and status to the client.

**Scaling the write path:**
- Keep the synchronous portion minimal (validate + persist); push notifications,
  analytics, receipts, and fulfillment onto events.
- Order service is stateless and horizontally scaled; DB uses connection
  pooling, and partitions/shards by customer or order id if write volume demands.
- Use the outbox pattern (write order + event in one transaction, relay to the
  bus) so an event is never lost between DB commit and publish.

## Front End

**Project organization:** feature-based structure — group by domain
(`features/cart`, `features/orders`, `features/catalog`), each with its own
components, hooks, and API calls, plus shared `components/`, `hooks/`, `lib/`,
`api/`. Server state via React Query; global UI/auth state via Context or a
lightweight store. Code-split by route.

**Router:** React Router (data router / `createBrowserRouter`) with route-level
lazy loading and protected routes that gate on the decoded JWT / auth context.

## Ops / Deployment

**What's in your YAML?** (Kubernetes manifests / Helm values)
- Deployment: image + tag, replica count, resource `requests`/`limits`,
  readiness & liveness probes, rolling-update strategy.
- Service + Ingress (routing, TLS).
- HorizontalPodAutoscaler (scale on CPU/RPS to handle the 100k concurrency).
- ConfigMaps for config; Secrets for keys/DB creds (or external secrets manager).
- For CI: pipeline YAML (build → test → scan → push image → deploy).

**Deploy to:** containers (Docker) on Kubernetes — EKS on AWS. Behind an ALB +
CloudFront (CDN) + WAF. Managed data services (RDS Postgres, ElastiCache Redis,
MSK/Kafka or SNS+SQS). Multi-AZ for availability.

## Observability

- **Logs:** structured JSON, centralized (CloudWatch / ELK), correlation id
  propagated from the gateway through every service.
- **Metrics:** RED metrics per service (rate, errors, duration) in Prometheus,
  dashboards in Grafana; business metrics (orders/min, checkout conversion).
- **Tracing:** distributed tracing (OpenTelemetry → Jaeger/X-Ray) so an order
  can be followed across gateway → order → payment → notification.
- Alerting on SLOs (p99 latency, error rate, queue depth).

## Key Decisions

- **RS256 over HS256** — public-key verification lets every service validate
  tokens without sharing a secret.
- **Claims for coarse roles, cached lookup for fine-grained perms** — balances
  token size / staleness against a lookup hop.
- **Async notifications via event bus + outbox** — decouples the order write
  path and guarantees the event fires.
- **Idempotency keys on order creation** — makes client retries safe under a
  flaky network at 100k users.

## What This Tests

Whether you can move from a broad "design an e-commerce site" prompt into
concrete mechanics on demand — JWT internals, gateway/service trust boundaries,
RBAC lookup trade-offs, and a scalable async order flow — while keeping the
system secure, scalable, and observable.
