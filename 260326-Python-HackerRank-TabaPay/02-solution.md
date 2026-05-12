---
title: Spell Check — Solution
---

## Approach

Count letter frequencies in the available set using `Counter`. For each word, count
its letter frequencies and check that every required count is ≤ the available count.
`Counter` subtraction handles this in one line: `word_count - available` is non-empty
only when the word needs a letter more times than available.

## Key Decisions

- `Counter` subtraction (`-`) drops zero/negative results, so `word_counter - available`
  is empty `{}` exactly when all requirements are satisfied — clean one-liner check.
- Strip whitespace from letters and words (input has spaces after commas).
- Output preserves the original word order from the input list.

## Edge Cases

- Word with a letter not in the available set: `Counter` subtraction yields a non-empty
  result, correctly rejected.
- Word needing a letter more times than available (e.g., two `a`s but only one available):
  subtraction yields `{'a': 1}`, correctly rejected.
- Empty word list: outputs nothing.

## Complexity

- Time: O(L + W·K) — L = available letters count, W = word count, K = avg word length
- Space: O(A) — A = distinct available letters (for the Counter)

## What This Tests

Multiset / frequency-map reasoning. Tests whether the candidate reaches for `Counter`
or implements a manual frequency comparison.
