# Verkada Interview Prep Plan

## Format
- Code Signal, 2 problems, 1 hour
- Custom questions, standard algorithm concepts
- Target: solve both problems correctly in 60 minutes

---

## Priority Stack (highest → lowest ROI for Verkada)

| Priority | Topic | Evidence | Sessions Needed |
|----------|-------|----------|-----------------|
| 1 | Intervals | 4-5 Glassdoor mentions (merge, intersect, motion periods) | 2-3 |
| 2 | Graph traversal (BFS/DFS) | Explicitly called out multiple times | 2 |
| 3 | Trees (level order, search) | Multiple mentions | 1-2 |
| 4 | Trie | Specific mention: create, insert, find endings | 1 |
| 5 | Merge sorted lists / K-way merge | 2 mentions | 1 |
| 6 | String recursion | Subsequence/pattern matching, hardest reported question | 1 |
| 7 | Topological sort | Lower signal but good advanced coverage | 1 |

---

## Phase 1: Intervals (2-3 sessions)

**Why first:** Most commonly cited topic at Verkada by far.

**Core skills to build:**
- Merge overlapping intervals
- Find gaps / uncovered ranges
- Intersect two sorted interval lists
- Intersect K sorted interval lists (harder variant)

**Key pattern:** Sort by start time, then sweep. Know when to merge vs. gap.

**Sessions:**
1. Merge overlapping intervals + find gaps (Verkada: motion periods)
2. Intersect two sorted interval lists
3. Intersect K lists (if time permits before interview)

---

## Phase 2: Graph Traversal (2 sessions)

**Why second:** Explicitly called out, appears in Code Signal format.

**Core skills to build:**
- BFS — shortest path, reachability within K hops
- DFS — cycle detection, connected components
- Visited set discipline (never a list)
- Deque for BFS (never a stack)

**Sessions:**
1. BFS — reachability / shortest path (Verkada: camera network)
2. DFS — cycle detection or connected components

---

## Phase 3: Trees (1-2 sessions)

**Core skills to build:**
- Level order traversal (BFS on tree)
- DFS search — find node, path sum, depth
- Recursive base cases

**Sessions:**
1. Level order traversal + tree search combined problem

---

## Phase 4: Trie (1 session)

**Core skills to build:**
- TrieNode class with `children` dict and `is_end` flag
- Insert word
- Search word
- Prefix search / iterate to find all endings

**Sessions:**
1. Build trie from scratch, insert, search, iterate

---

## Phase 5: Merge Sorted Lists / K-Way Merge (1 session)

**Core skills to build:**
- Merge two sorted lists (two pointers)
- K-way merge using a min-heap
- Heap tuple format: `(value, list_index, element_index)`

**Sessions:**
1. Two sorted lists → K sorted lists

---

## Phase 6: String Recursion (1 session)

**Core skills to build:**
- Subsequence / pattern matching with skipping
- Recursive structure: match head, recurse on tail
- Memoization to avoid recomputation

**Sessions:**
1. Pattern matching with skipping (reported as hardest Verkada question)

---

## Speed Targets (Code Signal format: 2 problems, 60 min)

| Time elapsed | Target |
|---|---|
| 5 min | Read both problems, choose order |
| 25 min | Problem 1 complete with basic tests |
| 50 min | Problem 2 complete with basic tests |
| 60 min | Edge cases reviewed, submit |

---

## Phase 7: Topological Sort (1 session)

**Core skills to build:**
- Kahn's algorithm (BFS with in-degree tracking)
- DFS post-order
- Cycle detection via topo sort
- Parallel waves / layered ordering

**Sessions:**
1. Alert rule ordering (problem already generated: `verkada_alert_rule_ordering.md`)

---

## What to Skip (lower ROI for Verkada)

- OOP system design (no evidence in Glassdoor data)
- Matrix / 2D grid problems (low signal)
- Dynamic programming (no mentions)

---

## Current Status

| Topic | Status |
|---|---|
| Intervals | ❌ Not started |
| Graph traversal | ❌ Not started |
| Trees | ❌ Not started |
| Trie | ❌ Not started |
| K-way merge | ❌ Not started |
| String recursion | ❌ Not started |
| Topological sort | ⬜ Problem generated (`verkada_alert_rule_ordering.md`) |
