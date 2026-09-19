# Analysis: Interview Problem Phase Framework

## Source
Derived from analysis of all interview sessions in this repository (March 2026).
Updated 2026-03-26: added TabaPay HackerRank session observations.
Updated 2026-05-11: added Mosaic take-home backend API session.
Updated 2026-05-20: added Axle fundamentals screen observations.
Updated 2026-06-12: added M.AI CodeSignal progressive UI screen.
Updated 2026-09-18: added Blue Shield system design session and SWE Open Call streaming screen.

## The core observation

Every human-interviewer algorithmic problem in this repo has multiple phases. The phases are not labeled "easy/medium/hard" — they escalate by changing *what the candidate is responsible for*.

**Automated screens (HackerRank):** do not follow the phase progression. Each problem
is self-contained, single-phase, and graded pass/fail. The phase framework applies to
live interview sessions only.

**Automated coding screens with hidden-test escalation (CodeSignal-style):** a variant
observed at SWE Open Call. A single stateful class (`feed`/`get_records` streaming parser),
graded on exact output against ~16 hidden test cases. There is no live interviewer, so the
escalation is *smuggled into the test suite*: the cases walk from the happy path (plain
objects) through malformed input, scalar values, escaped delimiters inside strings, deep
nesting, and records split across chunk boundaries. The candidate must enumerate these edge
classes unprompted — the "phases" exist, but only as hidden cases, not spoken requirements.

**Fundamentals/fluency screens:** a third format, observed at Axle — multiple small
Phase-1-only exercises in a single session. No progression, no search or optimization
phases. Tests whether a candidate can write basic Python correctly and quickly. These
sessions never reach Phase 2; the evaluation is speed and correctness of fundamentals.

**Progressive UI screens (CodeSignal):** a fourth automated format, distinct from
HackerRank. 4 levels unlock sequentially by passing a DOM-querying test suite. The
levels themselves escalate in front-end complexity (render → interact → fetch → sync),
but the phase framework maps differently: L1–2 are Phase 1 (render/mutate given data),
L3–4 are Phase 2 (find and fetch data yourself). No session in this format has
reached Phase 3 or 4. The test surface is CSS class names, not logic.

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
| Transaction Ledger | Parse stdin lines, accumulate totals into two dicts |
| Spell Check | For each word, check letter frequency against available pool |
| Mosaic bookstore | 5 CRUD endpoints — schema given, implement standard REST operations |
| Axle (4 exercises) | Divisible filter, dict merge with collision sum, dedup keep-first, dedup keep-last |
| M.AI L1 | Render tasks from JSON into 3 Kanban columns — data given, implement the display |
| M.AI L2 | Controlled form: validate, create task, clear fields — state given, mutate it |
| SWE Open Call | Streaming JSONL parser — buffer chunks, frame on newline, return completed records |

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
| M.AI L3 | Fetch tasks from API, filter by status; fetch user by ID for each task that has `assignedUser` |
| M.AI L4 | Update task status — find the task, mutate its state, re-render in new column |

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
| Mosaic bookstore | Concurrent award increments — lost update problem, atomic SQL vs. locking strategies |
| Blue Shield | E-commerce for 100k concurrent users — async order flow, JWT/RBAC, resumable 1 TB upload |

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
