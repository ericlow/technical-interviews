# Solution — Trailer Yard Part 0: JSON Parsing

## Shape
List of dicts → transform datetime string fields in place

## Solution

```python
import json
from datetime import datetime

def parse_events(filepath: str) -> list[dict]:
    with open(filepath, 'r') as f:
        events = json.load(f)

    for event in events:
        event['entrance_time'] = datetime.fromisoformat(event['entrance_time'])
        if event['exit_time'] is not None:
            event['exit_time'] = datetime.fromisoformat(event['exit_time'])

    return events

if __name__ == '__main__':
    events = parse_events('data.json')
    for e in events:
        print(e)
```

## Key decisions
- `datetime.fromisoformat()` — handles ISO 8601 strings cleanly in Python 3.7+
- Check `None` before parsing `exit_time` — null means trailer is still present
- Mutate in place — no need to construct new dicts for a warmup

## Phase analysis
Classic Phase 1: structure is given (JSON schema), operation is direct (parse string → datetime), no searching or optimization. The only complexity is the nullable field.
