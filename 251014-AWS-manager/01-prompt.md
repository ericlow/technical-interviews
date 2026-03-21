# AWS Manager — Cost-Effective GPU Reservation API (Go/Python)

## Type
Backend API coding challenge — REST API, concurrency, AWS SDK, business logic (1 hour)

## Problem

Build a RESTful API that queries AWS for GPU capacity block reservations across multiple regions concurrently and returns the single cheapest option.

## Endpoint

```
POST /reservations/find-cheapest
```

### Request body
```json
{
  "instance_type": "p4d.24xlarge",
  "instance_count": 2,
  "regions": ["us-east-1", "us-west-2", "eu-central-1"],
  "start_date": "2025-11-10",
  "required_duration_hours": 72
}
```

### Success response (200)
```json
{
  "capacityBlockOfferingId": "cb-0f7e8662751ff4036",
  "instanceType": "p5.48xlarge",
  "instanceCount": 1,
  "startDate": "2025-08-07T11:30:00Z",
  "endDate": "2025-08-08T10:30:00Z",
  "capacityBlockDurationHours": 24,
  "upfrontFee": 0,
  "currencyCode": "USD",
  "region": "us-east-1",
  "fee": 794.88
}
```

### Error responses
- `400 Bad Request` — invalid or missing parameters
- `404 Not Found` — no reservations available

## Business Logic

- **24-hour blocks**: AWS capacity blocks come in 24-hour increments only. Calculate minimum blocks needed for `required_duration_hours`.
- **Fixed start time**: Reservations always begin at **11:30 AM UTC** on `start_date`.
- **Spin-down period**: 1-hour mandatory spin-down at end of reservation (reduces usable hours per block).
- **Cost optimization**: From all results across all regions, return the one with lowest total price.

## Non-Functional Requirements

- **Concurrent regional queries**: Query all regions simultaneously, not sequentially.
- **Partial failure resilience**: If one region's query fails or times out, succeed using remaining regions' results. Do not fail the whole request.
- **Clean response**: Do not pass through raw AWS response — reshape to the schema above.

## AWS SDK

### Python (boto3)
```python
ec2_client = boto3.client("ec2", region_name="REGION")
ec2_client.describe_capacity_block_offerings(...)
# Errors: InvalidParameterValue, CapacityBlockDescribeLimitExceeded
```

### Go (aws-sdk-go-v2)
```go
regionClient := ec2.NewFromConfig(regionConfig)
regionClient.DescribeCapacityBlockOfferings(ctx, ...)
```

## Testing Requirements
- Happy path: cheapest reservation found
- Business logic: correct number of 24-hour blocks calculated
- Partial failure: one region fails, request succeeds with others
- Total failure: no reservations found → 404

## Deliverable
- Dockerized API exposing port 8080
