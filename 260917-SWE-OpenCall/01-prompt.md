# Streaming JSONL Ingestion

- **Source:** SWE Open Call (CodeSignal-style timed screen)
- **Date:** 2026-09-17
- **Stack:** Python 3
- **Type:** Algorithmic / OOP (streaming, stateful class)
- **Time box:** ~40 min, single problem, 16 hidden test cases

## Problem Statement (verbatim)

You're consuming a websocket stream of **JSONL** — JSON values separated by
newlines. The transport delivers arbitrary text chunks with no relationship to
the JSON structure. Users of your code must be able to access the data so far at
any time, even mid-stream.

Implement a class with:

- **`feed(chunk)`** — called each time new text arrives.
- **`getRecords()`** — callable **at any time**, including mid-stream. Returns
  every value fully received so far, in order.

### Example

```
feed('{"id":1,"na')
getRecords()  ->  []

feed('me":"alpha"}\n{"id":2}\n')
getRecords()  ->  ['{"id":1,"name":"alpha"}', '{"id":2}']
```

## Given Skeleton

```python
from typing import List

class StreamingJsonlParser:
    def __init__(self):
        pass

    def feed(self, chunk: str) -> None:
        """called each time new text arrives"""
        pass

    def get_records(self) -> List[str]:
        """callable at any time, including mid stream.
        Returns every value fully received so far, in order"""
        return []
```

> **Naming gotcha:** the prompt/driver call `getRecords()`, but the provided
> skeleton method is `get_records()`. The stdin driver dispatches on the tokens
> `feed` / `getRecords`; implement `get_records` (the harness maps the two).

## Constraints & Hidden-Test Requirements

The 16 hidden cases (input/expected were visible in the results panel) show the
records are framed **by newline**, not by braces, and that every value must be a
**complete, valid JSON value**. The cases exercised:

1. **Plain objects**, one per line — `{"id":1}\n{"id":2}\n`.
2. **A value split across many `feed()` calls** — `{"id"` … `:1,"t` … `ags":` …
   arriving one fragment at a time; nothing returned until the terminating `\n`.
3. **A malformed line is dropped** — feeding `{"x":[1,2}\n` (invalid) between two
   valid objects; `getRecords()` must skip it and still return the valid ones.
4. **Bare JSON scalars** — `true`, `false`, `null`, `42`, `"just a string"` are
   each valid records (no braces at all).
5. **Strings containing braces / escaped quotes** —
   `{"msg":"he said \"hi }\" to me"}` is one record; the `}` inside the string
   must not end it.
6. **Deep nesting** — `{"id":1,"tags":["a","b",{"deep":{"deeper":[1,2,3]}}]}` is
   a single record despite many inner braces.

`getRecords()` returns the **raw line strings** (e.g. `'true'`, `'42'`,
`'"just a string"'`), cumulative and in arrival order.
