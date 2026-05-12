---
title: Transaction Ledger — Solution
---

## Approach

Parse each line into (month, day, type, amount), accumulating totals into two
dictionaries keyed by `(month, day)` and `month` respectively. After reading all
input, sort each dictionary's keys numerically and print.

## Key Decisions

- Use `defaultdict(lambda: [0.0, 0.0])` where index 0 = G total, index 1 = P total.
  Avoids conditional initialization.
- Strip whitespace from each field — the example input has spaces after commas.
- Sort date keys as integer tuples `(month_int, day_int)` so `10/04 < 12/01` sorts
  correctly (string sort would also work here but is fragile).
- Missing type on a date prints `0.00` naturally because the default is `[0.0, 0.0]`.

## Edge Cases

- A date with only G transactions: P total remains `0.00` (default).
- Same date appearing non-consecutively in input: accumulation handles it.
- Floating-point accumulation: `round(..., 2)` at print time is sufficient for
  financial display; production code would use `decimal.Decimal`.

## Complexity

- Time: O(N log N) — dominated by sorting unique dates/months
- Space: O(N) — at most N unique date entries

## What This Tests

Basic stdin parsing, dictionary aggregation, and sort-then-print output formatting.
Equivalent to a warm-up problem testing attention to output format details.
