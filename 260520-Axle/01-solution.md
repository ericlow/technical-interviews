# Axle — Solution: Python Fundamentals

## Approach

Four standalone exercises testing core Python competency: iteration, parameterization, dictionary merging, and set-based deduplication. Problems escalate in subtlety — Exercise 2 surfaces a mutation/side-effect question, and Exercise 4 requires reasoning carefully about traversal direction to preserve relative order.

---

## Exercise 1 — Divisible Filter

**Core insight:** Iterate 1 through `limit` inclusive; keep values where `n % divisor == 0`. Phase 2 is a pure refactor — lift the hardcoded `3` and `20` into parameters.

**Complexity:** O(n) time, O(k) space where k is the count of matching numbers.

---

## Exercise 2 — Merge Dictionaries

**Core insight:** Walk all keys from both dicts, summing values on collision. The mutation-safe approach builds a fresh `result = {}` rather than modifying either input. The interview solution correctly identifies the side-effect risk in its docstring comment, but does mutate `short_dict` (whichever input was shorter).

**Cleaner approach:** union both key sets via `set(d1) | set(d2)`, then `result[k] = d1.get(k, 0) + d2.get(k, 0)`. No mutation, handles missing keys cleanly.

**Complexity:** O(n + m) time, O(n + m) space.

---

## Exercise 3 — Remove Duplicates (keep first)

**Core insight:** Forward pass with a `seen` set. Append to result only on first encounter; add to `seen` immediately. A set gives O(1) membership checks, keeping the overall pass linear.

**Complexity:** O(n) time, O(n) space.

---

## Exercise 4 — Remove Duplicates (keep last)

**Core insight:** Reverse the problem — iterate backward, apply the keep-first algorithm, then reverse the result. Equivalently: traverse from the back, accumulate into a list, call `reversed()` at the end.

The interview solution does exactly this and is clean. The invariant: after reversal, the last occurrence in the original order is the one that survives.

**Complexity:** O(n) time, O(n) space.

---

## Edge Cases

- Empty list / dict → return empty
- All identical elements (`[1, 1, 1]`) → `[1]` for both keep-first and keep-last
- Single element → unchanged
- Dicts with no overlapping keys → all values preserved, nothing summed

---

## What This Tests

Basic Python fluency, iteration patterns, set usage for O(1) membership checks, and awareness of mutation side effects when passing dictionaries as function arguments.
