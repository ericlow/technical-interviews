# Solution — AWS GPU Reservation API

## Shape
REST API + concurrent fan-out + filter/min aggregation

## Architecture

```
POST /reservations/find-cheapest
    → validate input
    → fan out: query all regions concurrently
    → collect results (tolerate partial failures)
    → filter valid offerings
    → return cheapest
```

## Business Logic

### Block calculation
```python
import math

SPINDOWN_HOURS = 1
BLOCK_SIZE_HOURS = 24

# Each 24-hour block has 1 hour spin-down, so usable hours = 23
# But the simpler interpretation: add spin-down to required, then ceil-divide
total_hours_needed = required_duration_hours + SPINDOWN_HOURS
num_blocks = math.ceil(total_hours_needed / BLOCK_SIZE_HOURS)
# e.g. 72 hours + 1 = 73 → ceil(73/24) = 4 blocks
```

### Start time
```python
from datetime import datetime, timezone

start_dt = datetime.strptime(start_date, "%Y-%m-%d").replace(
    hour=11, minute=30, tzinfo=timezone.utc
)
```

## Python Implementation (FastAPI + asyncio)

```python
import asyncio
import math
import boto3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone

app = FastAPI()

class ReservationRequest(BaseModel):
    instance_type: str
    instance_count: int
    regions: list[str]
    start_date: str
    required_duration_hours: int

async def query_region(region: str, req: ReservationRequest, num_blocks: int, start_dt: datetime):
    try:
        client = boto3.client("ec2", region_name=region)
        response = client.describe_capacity_block_offerings(
            InstanceType=req.instance_type,
            InstanceCount=req.instance_count,
            StartDateRange=start_dt.isoformat(),
            CapacityDurationHours=num_blocks * 24,
        )
        offerings = response.get("CapacityBlockOfferings", [])
        for o in offerings:
            o["region"] = region
        return offerings
    except Exception:
        return []  # partial failure: swallow, return empty

@app.post("/reservations/find-cheapest")
async def find_cheapest(req: ReservationRequest):
    if not req.regions or not req.instance_type or req.instance_count < 1:
        raise HTTPException(status_code=400, detail="Invalid parameters")

    num_blocks = math.ceil((req.required_duration_hours + 1) / 24)
    start_dt = datetime.strptime(req.start_date, "%Y-%m-%d").replace(
        hour=11, minute=30, tzinfo=timezone.utc
    )

    # Fan out concurrently
    results = await asyncio.gather(
        *[query_region(r, req, num_blocks, start_dt) for r in req.regions]
    )

    all_offerings = [o for region_results in results for o in region_results]

    if not all_offerings:
        raise HTTPException(status_code=404, detail="No reservations found")

    cheapest = min(all_offerings, key=lambda o: float(o.get("UpfrontTotalPrice", 0)))

    return {
        "capacityBlockOfferingId": cheapest["CapacityBlockOfferingId"],
        "instanceType": cheapest["InstanceType"],
        "instanceCount": req.instance_count,
        "startDate": cheapest["StartDate"],
        "endDate": cheapest["EndDate"],
        "capacityBlockDurationHours": cheapest["CapacityBlockDurationHours"],
        "upfrontFee": cheapest.get("UpfrontTotalPrice", 0),
        "currencyCode": cheapest.get("CurrencyCode", "USD"),
        "region": cheapest["region"],
        "fee": float(cheapest.get("UpfrontTotalPrice", 0)),
    }
```

## Key Design Decisions

- **asyncio.gather**: fans out all regional queries concurrently; each returns `[]` on failure (partial failure tolerance)
- **Swallow exceptions per region**: ensures one bad region can't fail the whole request
- **`min()` with key**: single-pass cheapest selection — no sorting needed
- **Pydantic for validation**: `400` comes for free if required fields are missing/wrong type
- **Reshape response**: raw AWS field names (PascalCase) mapped to clean camelCase output

## Testing

```python
# Happy path
mock all regions returning offerings → assert cheapest is returned

# Block calculation
assert ceil((72 + 1) / 24) == 4
assert ceil((24 + 1) / 24) == 2

# Partial failure
mock region A raises exception, B returns offering → assert B's offering returned

# Total failure
mock all regions raise → assert 404
```
