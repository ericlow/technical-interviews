# What to Expect from Algorithmic-Style Interviews

## Source
Derived from analysis of all interview sessions in this repository (March 2026).
Refresh by re-reading the `_meta/` files and all `{NN}-prompt.md` files, then regenerate.

---

## Format

- 45–60 minutes, one interviewer watching you think out loud
- 1–2 problems, almost always with progressive requirements
- You are expected to ask clarifying questions before coding
- Requirements are extended mid-session — this is intentional, not a surprise

---

## What interviewers are actually evaluating

- Can you recognize the shape of the problem before writing code?
- Do you validate your understanding before diving in?
- Can you ship a working Phase 1 quickly, then extend cleanly?
- Do you articulate *why* you made a decision, not just that you made it?
- How do you handle a requirement that breaks your previous assumptions?

---

## The hidden test

Phase 1 is rarely where candidates fail. They fail when Phase 2 arrives and their Phase 1 code can't be extended without rewriting it. The interviewer is watching whether your v1 is adaptable.

---

## Phase structure (observed across all sessions)

| Phase | What changes | Candidate responsibility |
|---|---|---|
| 1 | Nothing — simplest assumptions | Given the address, validate inputs, mutate state |
| 2 | Caller stops giving you the answer | Find it yourself — search, filter, automate |
| 3 | Correctness is no longer enough | Minimize or maximize a metric |
| 4 | Single machine model breaks | Scale, concurrency, failure modes |

**Phase 1 time target: 10–15 minutes.** If it's taking longer, something is overcomplicated.

---

## Problem shapes observed (and the right data structure for each)

| Shape | Natural structure | Example |
|---|---|---|
| "Given X, find Y" | dict | bank accounts, word counter |
| Objects with attributes and behavior | classes | parking garage |
| Hierarchical / parent-child | tree | stack profiler |
| Spatial / positional | 2D grid | block puzzle |
| Ordered sequence with time intervals | list of objects | trailer yard events |

**The real skill:** ask "what is the shape of this data?" before writing any code.

---

## Algorithmic patterns observed

### Command dispatch
A list of operations is processed sequentially. Each command has a type and arguments. Route by type, validate, mutate state, return result.
- Example: Bank (`CREATE`, `ADD`, `TRANSFER`)
- Phase 1 characteristic: one operation type, caller provides all addressing

### OOP simulation with progressive requirements
Classes are given or obvious. Implement operations against them. Each requirement adds a constraint or removes an assumption the previous requirement had.
- Example: Parking garage (basic park → size-aware → distance-optimized)
- Key risk: Phase 1 design that can't accommodate Phase 2 without a rewrite

### Stream aggregation
Events arrive one at a time. Maintain a running aggregate. Query the aggregate efficiently.
- Example: Word counter (`onTweet` → `getWordCount`)
- Natural structure: dict (word → count)

### Tree construction from flat input
Input is a flat list of paths or sequences. Output is a hierarchical tree with aggregated counts.
- Example: Stack trace profiler (list of traces → call tree)
- Natural structure: tree node with ordered-dict children

### Grid simulation
A 2D grid with entities and movement rules. Determine valid moves at each step.
- Example: Block puzzle (find any block with clear exit path)
- Natural structure: the grid itself (list of strings); block cells as list of (row, col) tuples

### Datetime interval overlap
Events have start and end times. Determine which events overlap a target date or window.
- Example: Trailer yard filter
- Key insight: equality check on date misses multi-day events; use interval overlap formula

---

## Greedy reasoning

A greedy algorithm makes the locally best decision at each step without looking ahead.

**When it's safe:** when a locally good choice cannot make future choices worse.
- Block puzzle: removing a block only clears space → greedy is safe
- Parking garage: picking closest spot doesn't affect other cars → greedy is safe

**What interviewers want to hear:** not just the choice, but the justification.
> "Greedy is safe here because removing a block is monotonically beneficial — it can only open options, never close them."

**Alternatives when greedy is not safe:**
- Backtracking: try a choice, undo if it leads to failure
- BFS: find shortest path over a state space
- Dynamic programming: cache overlapping subproblem results

---

## What interviewers ask about data structures

Not "which data structure did you use?" but:
- "Why that choice?"
- "What's the tradeoff?"
- "What would you use if the input were 100x larger?"

The signal they're looking for: you recognize when a linear scan needs to become a lookup (list → dict), and you can say why.

---

## Edge cases always come from the domain

Not contrived. The domain tells you what can go wrong:
- Same-account transfer (bank)
- Car already parked (garage)
- Null exit time — trailer still present (trailer yard)
- Non-contiguous block shapes (block puzzle)
- Punctuation attached to words (word counter)

**Before coding Phase 1:** list the domain-specific edge cases out loud. Interviewers evaluate thoroughness here, not just correctness.

---

## The extensibility principle

The real difficulty of these problems is not Phase 1. It is whether Phase 1 was written in a way that Phase 2 can be bolted on without a structural rewrite.

**Signs Phase 1 will break under Phase 2:**
- Hardcoded spot_id instead of a search
- Balance stored as a string instead of an int
- No secondary lookup dict — unparking requires O(n) scan
- Logic embedded in `__main__` instead of a method

**Signs Phase 1 is built to last:**
- Operations are methods on the right class
- State lives in one authoritative place
- Secondary lookups are introduced as soon as a second access pattern is needed
- Return values are typed consistently (all strings, or all ints — not mixed)
