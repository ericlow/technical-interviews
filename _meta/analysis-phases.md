# Analysis: Interview Problem Phase Framework

## Source
Derived from analysis of all interview sessions in this repository (March 2026).

## The core observation

Every algorithmic interview problem in this repo has multiple phases. The phases are not labeled "easy/medium/hard" — they escalate by changing *what the candidate is responsible for*.

---

## Phase 1 — Implement the direct operation

**Characteristic:** The caller has done the hard thinking for you. You are given the address of the thing to operate on. You validate inputs and mutate state.

**What you are NOT doing in Phase 1:**
- Choosing a data structure (it's given or trivially obvious)
- Searching for anything
- Optimizing anything
- Handling scale or concurrency

**Examples:**
| Problem | Phase 1 task |
|---|---|
| Parking garage | `park(spot_id, car)` — spot_id is given, just validate and assign |
| Bank | `CREATE` / `ADD` — account name given, just validate uniqueness and mutate balance |
| Trailer Yard | Parse JSON and deserialize datetime strings |
| Word counter | `onTweet(id)` — fetch, split, increment |

**Common mistake:** Jumping to Phase 2 logic before Phase 1 is clean. Interviewers notice.

**Time target:** 10–15 minutes. If it's taking longer, something is overcomplicated.

---

## Phase 2 — Find the answer yourself

**Characteristic:** The caller no longer gives you the address. You must search for it. Data structure choice becomes meaningful.

**What changes from Phase 1:**
- You choose which spot to use (not given `spot_id`)
- You search through a collection
- You introduce a secondary lookup structure

**Examples:**
| Problem | Phase 2 task |
|---|---|
| Parking garage | `autopark(car)` — find any compatible spot |
| Bank | `TRANSFER` — validate both accounts, check balance, mutate two records |
| Trailer Yard | Filter events by facility + date overlap (requires interval logic) |
| Stack profiler | Build the tree from flat traces (the whole algorithm) |

---

## Phase 3 — Optimize the search

**Characteristic:** Correctness is no longer enough. You must minimize or maximize something. Data structure choice now has performance implications.

**Examples:**
| Problem | Phase 3 task |
|---|---|
| Parking garage | `autopark` picks closest spot (minimize distance) |
| AWS manager | Return cheapest reservation across regions |
| Block puzzle | Find any valid exit (the greedy justification matters here) |

**Common discussion:** O(n) scan vs. heap/sorted structure. Interviewers may ask "how would you make this faster at scale?"

---

## Phase 4 — Scale and system design

**Characteristic:** The local, single-machine model is replaced with a distributed one. Concurrency, capacity planning, and failure modes enter the picture.

**Examples:**
| Problem | Phase 4 task |
|---|---|
| Everlaw | Database selection, capacity planning for 100M tweets |
| AWS manager | Concurrent multi-region queries with partial failure resilience |
| Supio | Scale to 1000 docs/day, LLM rate limits, DLQ strategy |

---

## The "CRUD is Phase 1" misconception

CRUD is one instance of Phase 1, but not all of it. The real defining characteristic is:

> **Phase 1 = implement the most direct version of the core operation under the simplest possible assumptions.**

Sometimes that's a create/read. Sometimes it's parsing a file. Sometimes it's incrementing a counter. What makes it Phase 1 is that no search, optimization, or scale reasoning is required.

---

## Practical use

When generating new practice problems, specify the phase explicitly:

```
Domain: library book reservation
Shape: collection of objects with attributes
Phase 1: reserve(book_id, user_id) — book_id given, validate availability and assign
Phase 2: find_book(title, author) — search by attributes
Phase 3: find_nearest_available(user_location) — optimize by distance
Phase 4: distributed inventory across multiple branches, eventual consistency
```

This gives a candidate a clear progression to work through, matching the structure of real interviews.
