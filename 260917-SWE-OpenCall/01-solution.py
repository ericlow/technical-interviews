"""Streaming JSONL Ingestion — SWE Open Call, 2026-09-17.

JSONL = JSON values separated by newlines, arriving in arbitrary text chunks.
The only reliable frame is the newline (JSONL forbids literal newlines inside a
value). Each complete line is validated with json.loads; malformed lines are
dropped. get_records() returns the raw line strings, cumulative and in order.
"""

import json
from typing import List


class StreamingJsonlParser:
    def __init__(self):
        self._buffer = ""
        self._records: List[str] = []

    def feed(self, chunk: str) -> None:
        """Called each time new text arrives."""
        self._buffer += chunk
        while "\n" in self._buffer:
            line, self._buffer = self._buffer.split("\n", 1)
            line = line.strip()
            if not line:
                continue
            try:
                json.loads(line)          # complete & valid JSON value?
            except ValueError:
                continue                  # skip malformed lines
            self._records.append(line)    # store the original text

    def get_records(self) -> List[str]:
        """Callable at any time. Every value fully received so far, in order."""
        return list(self._records)

    # The driver dispatches on the token `getRecords`; expose it as an alias.
    getRecords = get_records


def _check(label, got, expected):
    status = "ok " if got == expected else "FAIL"
    print(f"[{status}] {label}")
    if got != expected:
        print(f"       got:      {got}")
        print(f"       expected: {expected}")


if __name__ == "__main__":
    # Prompt example
    p = StreamingJsonlParser()
    p.feed('{"id":1,"na')
    _check("mid-value returns []", p.get_records(), [])
    p.feed('me":"alpha"}\n{"id":2}\n')
    _check("two objects", p.get_records(),
           ['{"id":1,"name":"alpha"}', '{"id":2}'])

    # Malformed line is dropped, valid ones kept
    p = StreamingJsonlParser()
    p.feed('{"a":1}\n')
    p.feed('{"x":[1,2}\n')          # malformed -> dropped
    p.feed('{"c":3}\n')
    _check("skip malformed", p.get_records(), ['{"a":1}', '{"c":3}'])

    # Bare scalars are valid records
    p = StreamingJsonlParser()
    p.feed('true\nfalse\nnull\n42\n"just a string"\n{"ok":1}\n')
    _check("scalars", p.get_records(),
           ['true', 'false', 'null', '42', '"just a string"', '{"ok":1}'])

    # String containing an escaped quote and a brace
    p = StreamingJsonlParser()
    p.feed('{"msg":"he said \\"hi }\\" to me"}\n')
    _check("brace inside string", p.get_records(),
           ['{"msg":"he said \\"hi }\\" to me"}'])

    # Deep nesting, fed one fragment at a time
    p = StreamingJsonlParser()
    for frag in ['{"id"', ':1,"t', 'ags":', '["a",', '"b",{',
                 '"deep', '":{"d', 'eeper', '":[1,', '2,3]}', '}]}', '\n']:
        p.feed(frag)
    _check("deep nested split across feeds", p.get_records(),
           ['{"id":1,"tags":["a","b",{"deep":{"deeper":[1,2,3]}}]}'])
