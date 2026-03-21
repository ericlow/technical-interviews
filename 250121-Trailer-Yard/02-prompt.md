# Trailer Yard Invoicing — Part 1: Date + Facility Filter (Python)

## Type
Python coding — datetime interval overlap, filtering (30 min target)

## Problem

Given the trailer events from Part 0, write a function that returns all events for trailers that were at a given facility on a given date.

## Function signature

```python
def filter_events(events: list[dict], date: date, facility_id: int) -> list[dict]:
    ...
```

## Example

Filter for **January 18, 2022** at **facility 1** → should return **18 events**.

## Rules

- A trailer "was at the facility on date D" if its time at the facility **overlaps** with date D
- `exit_time` may be `null` — trailer is still present (treat as still there on any future date)
- Filter by both `facility_id` AND date overlap

## The tricky part

This is an **interval overlap** problem. A trailer event spans `[entrance_time, exit_time]`. Date D spans `[D 00:00:00, D 23:59:59]`. The event overlaps with D if:

```
entrance_time <= end_of_day(D)  AND  (exit_time is None OR exit_time >= start_of_day(D))
```

## Time target
30 minutes (cumulative from start of interview)
