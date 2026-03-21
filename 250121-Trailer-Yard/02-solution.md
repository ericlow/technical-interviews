# Solution — Trailer Yard Part 1: Date + Facility Filter

## Shape
List of event objects → filter by facility + datetime interval overlap

## Core insight

This is an interval overlap problem, not a simple equality check. A trailer event [entrance, exit] overlaps with day D if it was present at ANY point during that day. The overlap condition:

```
entrance_time < start_of_day(D+1)   # entered before day ended
AND
(exit_time is None OR exit_time >= start_of_day(D))  # hadn't left before day started
```

Equivalently: `entrance <= end_of_day(D)` and `exit >= start_of_day(D)`.

## Solution

```python
from datetime import datetime, date, timezone

def filter_events(events: list[dict], target_date: date, facility_id: int) -> list[dict]:
    # Build day boundaries (timezone-aware if events use UTC)
    day_start = datetime(target_date.year, target_date.month, target_date.day,
                         tzinfo=timezone.utc)
    day_end = datetime(target_date.year, target_date.month, target_date.day,
                       23, 59, 59, tzinfo=timezone.utc)

    result = []
    for event in events:
        if event['facility_id'] != facility_id:
            continue

        entrance = event['entrance_time']
        exit_time = event['exit_time']

        entered_before_day_ended = entrance <= day_end
        still_present_or_left_after_day_started = (
            exit_time is None or exit_time >= day_start
        )

        if entered_before_day_ended and still_present_or_left_after_day_started:
            result.append(event)

    return result
```

## Why the naive approach fails

A beginner might check `entrance_time.date() == target_date`. This misses trailers that:
- Entered the day before and were still present on target_date
- Entered on target_date and left the next day

The interval overlap formulation catches all cases.

## Phase analysis
- **Phase 1 (Part 0)**: Structure given, direct transformation, no logic
- **Phase 2 (Part 1)**: Must reason about time intervals, not just equality. The data structure (list of dicts) is the same — the complexity is in the predicate logic.

## Patterns
- Interval overlap: `A overlaps B iff A.start <= B.end AND A.end >= B.start`
- Null-as-infinity: `exit_time is None` treated as "still ongoing"
- Timezone awareness: ensure datetime comparisons are consistent (both UTC or both naive)
