# Trailer Yard Invoicing — Part 0: JSON Parsing (Python)

## Type
Python coding — warmup, data deserialization (15 min target)

## Company
Baton (same company as the sliding block puzzle)

## Problem

Parse a JSON file of trailer yard events and deserialize the datetime string fields into proper datetime objects.

## Event schema

```json
{
  "id": <number>,
  "trailer_id": <number>,
  "facility_id": <number>,
  "entrance_time": <string>,   // ISO datetime string
  "exit_time": <string> | null // ISO datetime string or null (trailer still present)
}
```

## Task

Write a function that:
1. Reads and parses the JSON file
2. Deserializes `entrance_time` and `exit_time` strings to `datetime` objects
3. Handles `exit_time: null` (trailer has not yet exited)
4. Returns the full dataset with deserialized values

Print the result to verify.

## Time target
15 minutes
