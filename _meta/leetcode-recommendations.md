# LeetCode Recommendations by Interview

Recommendations derived from reviewing each interview's problem structure. For each problem: difficulty, confidence that it's related, and reasoning.

## Practice Set

Already in rotation (no need to add):
- 57 — Insert Interval ✓
- 56 — Merge Intervals ✓
- 435 — Non-Overlapping Intervals ✓
- 252 — Meeting Rooms ✓
- 253 — Meeting Rooms II ✓

---

## Bank (241104) — Command Dispatch + Dict State

**Core skills:** hash map state, command dispatch, validate→mutate→record, transaction history.

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 2043 — Simple Bank System | Medium | Very High | Literally the same problem: bank accounts, deposit/withdraw/transfer, return `""` on invalid |
| 1396 — Design Underground System | Medium | High | Command-style operations updating multiple dicts in sync; check-in/check-out → validate → record |
| 355 — Design Twitter | Medium | High | OOP with per-entity history lists; dual-dict approach mirrors `accounts/history` |
| 146 — LRU Cache | Medium | Medium | Dict-backed stateful system; tests "multiple dicts in sync" discipline |
| 1472 — Design Browser History | Medium | Medium | Simple state mutation with sequential operations — good warmup for Level 1 command structure |

**Best prep path:** 2043 → 1396 → 355

---

## Baton (250105) — Sliding Block Puzzle

**Core skills:** grid parsing, path-clear checking in 4 directions, greedy removal order, BFS state search.

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 200 — Number of Islands | Medium | High | Grid component identification — finding which cells belong to a block |
| 490 — The Maze | Medium | High | Ball slides in a direction until it hits a wall — direct analog to block sliding |
| 505 — The Maze II | Medium | High | Sliding mechanic with distance optimization — extension of 490 |
| 773 — Sliding Puzzle | Hard | High | BFS over board states to find valid move sequence — covers the search-required case |
| 1263 — Minimum Moves to Move a Box | Hard | High | Multi-cell object sliding on a grid — closest structural analog to multi-cell blocks |
| 286 — Walls and Gates | Medium | Medium | Multi-source BFS for reachability — "can this block exit?" intuition |
| 752 — Open the Lock | Medium | Medium | BFS on discrete state space — right mental model if greedy fails |

**Best prep path:** 200 → 490 → 505 → 773

---

## Trailer Yard (250121) — Datetime Interval Overlap

**Note:** Part 0 (JSON/datetime parsing) has no LeetCode analog — Python stdlib exercise. All recommendations cover Part 1.

**Core skill:** interval overlap: `A.start <= B.end AND A.end >= B.start`.

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 252 — Meeting Rooms | Easy | Very High | Core interval overlap check — exactly the condition used in Part 1 |
| 253 — Meeting Rooms II | Medium | High | Interval sweep; extends overlap check to counting simultaneous intervals |
| 56 — Merge Intervals | Medium | High | Sort + sweep; trains start/end boundary reasoning |
| 986 — Interval List Intersections | Medium | High | Two-pointer intersect — scales the Part 1 pattern to range queries |
| 1229 — Meeting Scheduler | Medium | High | Find overlapping free time; null exit_time maps to open-ended interval handling |
| 57 — Insert Interval | Medium | Medium | Builds before/overlap/after trichotomy edge case intuition |

**Best prep path:** 252 → 56 → 986 → 1229

---

## Sentry (260130) — Trie + OOP Design

### Problem 1: Stack Trace Profiler

**Core skills:** trie-like tree from sequences, DFS traversal for rendering, insertion-order children.

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 208 — Implement Trie | Medium | High | Exact same mechanic: walk sequences top-down, create nodes on first visit |
| 211 — Design Add and Search Words | Medium | High | Trie with traversal; same insertion pattern |
| 588 — Design In-Memory File System | Hard | High | Trie + ordered children + hierarchical display — nearly identical structure |
| 297 — Serialize and Deserialize Binary Tree | Hard | Medium | DFS traversal + reconstruction; the render phase is essentially DFS serialization |
| 745 — Prefix and Suffix Search | Hard | Medium | Trie variant with compound keys |

**Best prep path:** 208 → 211 → 588

### Problem 2: Parking Garage

**Core skills:** OOP class design, greedy minimum selection, progressive requirement extension, hash map for O(1) lookup.

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 1603 — Design Parking System | Easy | Very High | Literally a parking system with size buckets — direct warm-up |
| 1845 — Seat Reservation Manager | Medium | High | Greedy: always assign smallest available seat; min-heap maps to autopark distance optimization |
| 855 — Exam Room | Hard | High | Seat assignment with distance optimization — same greedy distance reasoning as Requirements 3 & 4 |
| 460 — LFU Cache | Hard | Medium | Complex OOP with multiple hash maps in sync — same challenge as `spots` + `parkedCars` |
| 1166 — Design File System | Medium | Medium | OOP with path lookup and validation; similar guard-clause pattern |

**Best prep path:** 1603 → 1845 → 855

---

## Verkada (260322) — Prep Plan Topics

No interview has occurred yet. Recommendations organized by prep plan priority.

### Priority 1 — Intervals

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 56 — Merge Intervals | Medium | Very High | Foundation: sort by start, sweep to merge |
| 986 — Interval List Intersections | Medium | Very High | Intersect two sorted interval lists — directly cited in prep plan |
| 759 — Employee Free Time | Hard | High | K sorted interval lists → find gaps; hardest interval variant |
| 57 — Insert Interval | Medium | High | Edge case coverage: before/overlap/after trichotomy |

### Priority 2 — Graph BFS/DFS

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 207 — Course Schedule | Medium | High | DFS cycle detection on a directed graph |
| 994 — Rotting Oranges | Medium | High | Multi-source BFS — reachability within K steps; camera-network analog |
| 542 — 01 Matrix | Medium | High | Multi-source BFS with distance tracking |
| 323 — Number of Connected Components | Medium | High | DFS connected components |

### Priority 3 — Trees

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 102 — Binary Tree Level Order Traversal | Medium | Very High | BFS on tree — explicitly in prep plan |
| 112 — Path Sum | Easy | High | DFS with recursive base cases |
| 437 — Path Sum III | Medium | High | Prefix sum + DFS; harder tree search variant |

### Priority 4 — Trie

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 208 — Implement Trie | Medium | Very High | Build from scratch, insert, search — directly cited |
| 211 — Design Add and Search Words | Medium | High | Prefix search + wildcard — extends 208 |
| 212 — Word Search II | Hard | High | Trie + grid DFS; "find all endings" variant |

### Priority 5 — K-Way Merge

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 21 — Merge Two Sorted Lists | Easy | Very High | Two-pointer foundation |
| 23 — Merge K Sorted Lists | Hard | Very High | Min-heap merge — directly cited in prep plan |
| 373 — Find K Pairs with Smallest Sums | Medium | High | Heap tuple format `(value, i, j)` — same pattern |

### Priority 6 — String Recursion / Pattern Matching

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 44 — Wildcard Matching | Hard | High | Subsequence matching with skip — "hardest reported question" analog |
| 10 — Regular Expression Matching | Hard | High | Recursive pattern match with memoization — same structure |
| 115 — Distinct Subsequences | Hard | High | Counts pattern embeddings in string — same recursive decomposition |

### Priority 7 — Topological Sort

| LeetCode Problem | Difficulty | Confidence | Reasoning |
|---|---|---|---|
| 207 — Course Schedule | Medium | Very High | Kahn's algorithm + cycle detection |
| 210 — Course Schedule II | Medium | Very High | Returns topological order; adds layered ordering requirement |
| 310 — Minimum Height Trees | Medium | High | Iterative leaf-trimming = Kahn's in disguise; parallel-wave intuition |
