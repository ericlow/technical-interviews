# Streaming JSONL Ingestion — Solution

## Core Insight

**JSONL is framed by the newline, not by the JSON structure.** The trap is that
a JSON object *looks* like it starts at `{` and ends at `}`, inviting a
brace-matching solution. Brace matching fails because:

- Records can be bare scalars (`true`, `42`, `"str"`) with **no braces**.
- A `}` can appear **inside a string** (`"he said }"`).
- Objects **nest**, so the first `}` is not the record's `}`.

The one delimiter you can trust is `\n`, because JSONL forbids literal newlines
inside a value (they must be escaped as `\n`). So the algorithm is:

1. Append every `chunk` to a running buffer.
2. While the buffer contains a `\n`, cut off the line before it.
3. That line is a **complete** record *iff* it parses as JSON — validate with
   `json.loads`. If it parses, store the **original line text**; if not
   (e.g. a malformed `{"x":[1,2}`), skip it.
4. Keep the trailing remainder (no `\n` yet) in the buffer for the next `feed`.
5. `get_records()` returns the accumulated list, in order.

Return the **raw strings**, not parsed objects — the expected output shows
`true`, `42`, `"just a string"` verbatim (parsed objects would print as `True`,
`42`, `just a string`).

## Reference Implementation

```python
import json
from typing import List

class StreamingJsonlParser:
    def __init__(self):
        self._buffer = ""
        self._records: List[str] = []

    def feed(self, chunk: str) -> None:
        self._buffer += chunk
        while "\n" in self._buffer:
            line, self._buffer = self._buffer.split("\n", 1)
            line = line.strip()
            if not line:
                continue
            try:
                json.loads(line)          # completeness/validity check
            except ValueError:
                continue                  # skip malformed lines
            self._records.append(line)    # store the ORIGINAL text

    def get_records(self) -> List[str]:
        return list(self._records)
```

## Key Decisions

- **Frame on `\n`, validate with `json.loads`.** Newline gives framing;
  `json.loads` gives the "is it a *complete, valid* value" check for free — no
  hand-rolled brace/string/escape state machine needed.
- **Store the raw line, not the parsed object.** Matches the expected string
  output and avoids re-serialization differences (key order, spacing, `True`
  vs `true`).
- **Skip malformed lines instead of raising.** A newline-terminated line that
  fails to parse is dropped; surrounding valid records are still returned.
- **Only split on a `\n` that has actually arrived.** A value split across
  chunks stays buffered until its newline shows up, so `get_records()` returns
  `[]` mid-value.

## Edge Cases

- Value split across arbitrary `feed()` boundaries → buffered, emitted on `\n`.
- Multiple complete values in one `feed()` → the `while` loop drains them all.
- Blank lines → skipped.
- `}` inside a string / escaped quotes → irrelevant; only `\n` frames.
- Deeply nested structures → irrelevant; one line = one value.
- Malformed newline-terminated line → dropped.
- `get_records()` mid-stream → returns whatever completed so far.

## Complexity

- `feed`: O(k) amortized for k characters added (buffer slicing + one
  `json.loads` per completed line). `json.loads` is O(line length).
- `get_records`: O(n) to copy the list of n records (O(1) if returning a
  reference is acceptable).
- Space: O(size of the current unterminated buffer + total stored records).

## What This Tests

Recognizing the right **framing** for a streaming protocol (newline-delimited
JSONL) and resisting the urge to hand-roll a structural parser. Secondary: robust
**buffering of state across arbitrary chunk boundaries**, handling all JSON value
types, and validating completeness with the standard library.
