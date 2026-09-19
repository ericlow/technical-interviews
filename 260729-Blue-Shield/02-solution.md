# Backend Domain Quickfire — Solution

## Q1 — Reducing Microservice Chatter

**Core insight:** the cost is the *number of synchronous network hops* on the
critical path. Cut hops, batch them, or move the data closer.

Techniques, roughly in order of leverage:

1. **API composition / aggregator (BFF or gateway).** Instead of the client (or
   each service) calling all 6 in a chain, put one aggregator that fans out the
   calls **in parallel** and composes the result. Turns a serial chain into one
   round trip from the caller's view.
2. **Batch / coarse-grained APIs.** Replace many chatty fine-grained calls
   (`get` one item at a time) with a bulk endpoint (`getMany`). Fewer, larger
   requests beat many small ones.
3. **Caching.** Cache hot, read-mostly data (Redis/ElastiCache, or in-service
   cache) so repeated `get`s don't hit the owning service every time.
4. **Async / event-driven instead of request-response.** For work that doesn't
   need an immediate answer, publish an event and let services react. Removes the
   synchronous dependency entirely.
5. **Data locality / CQRS read models.** Maintain a denormalized read model
   (materialized view) fed by events, so the reading service has the data
   locally and doesn't call out at all.
6. **Reconsider the boundaries.** If 6 services must always be called together
   for one action, that's a sign the decomposition is wrong — services that
   change and are invoked together may belong merged. Chattiness is often a
   design smell.
7. **Keep it in-region / same cluster and use gRPC** over a service mesh —
   binary protocol + connection reuse reduces per-call overhead vs REST/JSON,
   and co-location cuts latency.

**Short answer to give:** aggregate + parallelize the fan-out, add batch
endpoints and caching, go async where a response isn't needed, and if they're
*always* called together, question whether they should be separate services.

## Q2 — Resumable 1 TB Upload

This is the **multipart / chunked upload** pattern (exactly what S3 Multipart
Upload implements).

**How do you divide the file?**
- Split into fixed-size **chunks/parts** (e.g. 64 MB–256 MB each). Part size is
  a trade-off: bigger parts = fewer requests but more to re-send on failure;
  smaller parts = more overhead but cheaper retries. 1 TB / 128 MB ≈ 8,000
  parts.
- Each part has a **part number** (its ordinal position) so the server can
  reassemble in order.

**How do you track the parts?**
- Start an upload session → get an **upload id**. All parts reference it.
- For each uploaded part, the server returns an identifier (S3 returns an
  **ETag**, typically the part's checksum). The client keeps a manifest of
  `{partNumber → ETag/checksum, status}`.
- Track state per part: `pending / uploaded / verified`. This manifest is what
  makes the upload **resumable** — on reconnect, ask the server which parts it
  already has (S3: `ListParts`) and upload only the missing ones.

**You don't want to duplicate — what part do you restart?**
- Only restart the parts that **failed or never completed** — never re-upload
  parts already confirmed. The part number + upload id makes each part
  **idempotent**: re-sending the same part number just overwrites/no-ops rather
  than appending a duplicate.
- Use a **checksum per part** (and a whole-file checksum at the end) to verify
  integrity, so a corrupted part is detected and re-sent while good parts stay.
- When all parts are present, issue a **complete** call with the ordered list of
  part numbers + ETags; the server assembles the final object. If abandoned,
  issue **abort** to clean up (or a lifecycle rule to garbage-collect orphaned
  parts).

**Extras worth mentioning:** upload parts in parallel for throughput; use
pre-signed URLs so clients upload directly to S3 without proxying 1 TB through
your service; resume by persisting the manifest client-side so a crash doesn't
lose progress.

## What This Tests

Recognizing two named patterns on sight — API composition / anti-chatter tactics
for microservice fan-out, and idempotent, resumable **multipart upload** (S3
Multipart) with per-part tracking and checksums for the large-file case.
