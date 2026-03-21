# Solution — DoorDash Food Review System Design

## Architecture

```
App → LB → API Gateway → Review Service → Redis (cache)
                                        ↓
                                      Kafka
                                        ↓
                                  Review Writer → PostgreSQL
                                        ↑
                               EventBridge → Job Aggregator
CDN (static assets)
```

## Components

**Review Service** — handles all API requests
- Writes new reviews to PostgreSQL via Review Writer
- Reads item details/aggregated ratings from Redis cache (low latency reads)
- Publishes events to Kafka on new review submission

**Redis** — caches aggregated item ratings and item detail pages
- Serves `GET /v1/items/{id}/detail` with < 0.2 sec latency
- Invalidated/updated by the aggregation job

**Kafka** — message bus for review events
- Decouples write path from aggregation
- Allows eventual consistency for aggregation (hours)

**Review Writer** — Kafka consumer, writes reviews to PostgreSQL

**PostgreSQL** — source of truth for all data

**EventBridge + Job Aggregator** — scheduled aggregation job
- Triggered periodically (e.g. every few hours)
- Recalculates avg rating per item using incremental formula:

```
NewReviewCount   = sum of new reviews
NewReviewPoints  = sum of new rating points
CalcReviewCount  = oldReviewCount + newReviewCount
CalcReviewPoints = oldReviewPoints + newReviewPoints
CurrentRating    = CalcReviewPoints / CalcReviewCount
→ store back to Items table + invalidate Redis cache
```

**CDN** — serves static frontend assets

## Key Design Decisions

- **Reviews immutable**: no UPDATE path needed for reviews
- **Aggregate stored on Item**: avoids expensive aggregation at read time; updated async
- **Eventual consistency for aggregation**: acceptable per NFRs — ratings can lag hours
- **Redis for read latency**: < 0.2 sec requirement met by cache; cache refreshed by aggregation job
- **Kafka for write durability**: review not lost if downstream is slow; writer consumes independently
