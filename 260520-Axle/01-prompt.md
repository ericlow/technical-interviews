# Axle — Technical Screen: Python Fundamentals

**Source:** Axle  
**Date:** 2026-05-20  
**Stack:** Python  
**Type:** Algorithmic  

---

## Problem Statement

Four progressive Python exercises completed in a live screen-share session.

---

## Exercise 1 — Divisible Filter

**Phase 1:** Write a function that returns all numbers from 1–20 that are divisible by 3.

**Phase 2:** Generalize so both the upper limit and the divisor are parameters.

**Example:**
```
return_divisibleby3(20, 3) → [3, 6, 9, 12, 15, 18]
```

---

## Exercise 2 — Merge Dictionaries

Merge two integer-keyed dictionaries. If both dictionaries share a key, sum the values.

**Example:**
```
d1 = {1: 10, 2: 20}
d2 = {2: 30, 3: 40, 4: 50}
merge(d1, d2) → {1: 10, 2: 50, 3: 40, 4: 50}
```

**Key design question raised by interviewer:** Should the function mutate one of the input dictionaries, or return a fresh one?

---

## Exercise 3 — Remove Duplicates (keep first)

Given a list of integers, remove duplicates while preserving the original order. The **first** occurrence of each value should remain.

**Example:**
```
[0, 1, 2, 0, 3, 0] → [0, 1, 2, 3]
```

---

## Exercise 4 — Remove Duplicates (keep last)

Same as Exercise 3, but retain the **last** occurrence of each duplicate instead of the first.

**Example:**
```
[0, 1, 2, 0, 3, 0] → [1, 2, 3, 0]
```

---

## Constraints

- Python (any version)
- No external libraries required
- Values are integers
