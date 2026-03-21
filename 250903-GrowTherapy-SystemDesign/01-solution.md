# Solution — Grow Therapy System Design

## Architecture

```
Browser → Load Balancer → API Gateway → [book service, app service]
                                              ↓               ↓
                                      Calendar Provider    PostgreSQL
```

## Components

**Load Balancer** — distributes traffic, handles failover (fault tolerance)

**API Gateway** — routing, auth, rate limiting

**Book Service** — handles `/book` and `/provider/{id}/availability`
- Calls third-party Calendar Provider API for real-time availability
- Writes booking records to PostgreSQL

**App Service** — handles `/search`, `/provider`, `/provider` (CRUD)
- Reads/writes provider data from PostgreSQL
- Search queries filter by location (PostGIS or indexed lat/lng)

**PostgreSQL** — primary datastore
- Strongly consistent (satisfies consistency over availability requirement)
- Provider profiles, bookings stored here

**Calendar Provider** (third-party) — source of truth for provider availability slots

## API Design

```
GET  /search?location={location}&page={pageId}
     → Partial<Provider>[]

GET  /provider/{id}
     → Provider

POST /provider
     body: { name, location, description, specialties: [] }
     → 201

GET  /provider/{id}/availability?pageId=...&dateStart=...&dateEnd=...
     → AppointmentSlot[]

POST /book
     → BookingConfirmation
```

## Key Design Decisions

- **Consistency over availability**: PostgreSQL (CP system). No eventual consistency / caching on provider data that could mislead booking decisions.
- **Low latency < 0.5s**: Direct DB reads with proper indexing. No async pipelines on the read path.
- **Third-party calendar**: Called at read time for availability (real-time). Not cached aggressively to avoid stale slots.
- **Fault tolerance**: Load balancer with health checks, multiple app service instances. DB replicas for read redundancy.
