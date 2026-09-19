# What to Expect from Algorithmic-Style Interviews

## Source
Derived from analysis of all interview sessions in this repository (March 2026).
Updated 2026-03-26: added TabaPay HackerRank session.
Updated 2026-05-11: added Mosaic take-home backend API session.
Updated 2026-05-20: added Axle fundamentals screen.
Updated 2026-06-12: added M.AI CodeSignal progressive UI screen.
Updated 2026-09-18: added Blue Shield system design session and SWE Open Call streaming screen.
Refresh by re-reading the `_meta/` files and all `{NN}-prompt.md` files, then regenerate.

---

## Format

**Live interview (human interviewer):**
- 45–60 minutes, one interviewer watching you think out loud
- 1–2 problems, almost always with progressive requirements
- You are expected to ask clarifying questions before coding
- Requirements are extended mid-session — this is intentional, not a surprise

**Automated screening (HackerRank, similar platforms):**
- Multiple self-contained problems (no progressive requirements)
- Pass/fail test cases — output format must be exact
- Graded on correctness and edge case coverage, not design decisions
- Focus: clean Phase 1 implementation, stdin/stdout parsing, output formatting

**Automated coding screen with hidden-test escalation (CodeSignal-style):**
- A single stateful class (methods called in sequence by a stdin driver)
- Graded on exact output against ~16 hidden test cases; "All test cases failed" is binary and blunt
- No interviewer, so requirement escalation is *hidden in the test cases* — happy path first,
  then malformed input, edge types, and adversarial inputs
- Focus: enumerate edge classes yourself before submitting; frame the problem correctly first
- Example: SWE Open Call — `StreamingJsonlParser` (`feed`/`get_records`), newline-framed JSONL

**Take-home backend API project:**
- 60–90 minutes; full REST API with a relational database
- You own the stack choice; schema design and API design both evaluated
- Progressive stretch goals replace live phase escalation
- Concurrency and schema correctness are explicitly tested — not just correctness of output
- Example: Mosaic bookstore (CRUD + concurrent award increments + optional soft deletes/pagination)

**Fundamentals / fluency screen (live):**
- 4–6 short exercises, each 5–10 minutes
- No phase escalation — every exercise is Phase 1 only
- Tests basic Python syntax, built-in usage, and traversal direction reasoning
- Speed and correctness both matter; design decisions are minimal
- Example: Axle — divisible filter, dict merge, dedup keep-first, dedup keep-last

**Progressive UI screen (CodeSignal):**
- 4 locked levels; each unlocks by passing the current level's automated test suite
- Test suite queries the DOM via CSS selectors — exact class names are the contract
- 90 minutes; escalates render → interact → async fetch → state mutation
- Phase ceiling: Phase 2 (no optimization, no distribution)
- Example: M.AI — Kanban board, 4 levels, React/TypeScript

---

## What interviewers are actually evaluating (live sessions)

- Can you recognize the shape of the problem before writing code?
- Do you validate your understanding before diving in?
- Can you ship a working Phase 1 quickly, then extend cleanly?
- Do you articulate *why* you made a decision, not just that you made it?
- How do you handle a requirement that breaks your previous assumptions?

---

## The hidden test

Phase 1 is rarely where candidates fail. They fail when Phase 2 arrives and their Phase 1 code can't be extended without rewriting it. The interviewer is watching whether your v1 is adaptable.

---

## Phase structure (observed across all live sessions)

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
| "Can this request be satisfied by the pool?" | Counter / frequency dict | spell check |
| Two tables in sync, one denormalized from the other | relational DB + atomic SQL | Mosaic bookstore (`num_total_awards`) |
| Ordered list with duplicate values — keep first or last occurrence | set (seen) + traversal direction | Axle dedup exercises |
| List of items with optional foreign-key enrichment from a secondary API | useEffect + Promise.all + conditional render | M.AI L3 (tasks + user names) |
| User creates items that must appear immediately in a sibling component | controlled form + state lifted to common ancestor | M.AI L2 (create task form) |
| Stream of arbitrary chunks that must be framed into records | buffer + protocol delimiter + completeness validation | SWE Open Call (streaming JSONL parser) |

**The real skill:** ask "what is the shape of this data?" before writing any code.

---

## Two problem types — know which one you're facing

Not all problems in this repo are the same kind of challenge. Misidentifying the type
leads to solving the wrong problem.

**Algorithmically-core:** the domain is real-world but the challenge is a recognizable
CS algorithm. Recognize the pattern, implement it cleanly.
- Stack trace profiler → tree construction (trie variant)
- Block puzzle → greedy grid traversal
- Word counter → stream aggregation into a dict
- Transaction Ledger → stdin aggregation with sort-then-print
- Spell Check → multiset frequency check (Counter subtraction)

**Systems-core:** the algorithm is trivial (O(n) at most); the challenge is OOP design,
state placement, and extensibility under Phase 2.
- Parking garage, bank account → applied OOP with progressive requirements
- Trailer yard → interval logic in a real domain

Sentry asked both types in the same session. When you see a problem, ask first:
*"Is the hard part the algorithm, or the design?"*

---

## Algorithmic patterns observed

### Command dispatch
Route by operation type, validate, mutate state, return result.
- Example: Bank (`CREATE`, `ADD`, `TRANSFER`)

### OOP simulation with progressive requirements
Interface given upfront. Each phase adds a constraint or removes an assumption.
- Example: Parking garage (basic park → size-aware → distance-optimized)
- Key risk: Phase 1 design that can't accommodate Phase 2 without a rewrite

### Stream aggregation
Events arrive one at a time. Maintain a running aggregate. Query efficiently.
- Example: Word counter (`onTweet` → `getWordCount`) — natural structure: dict
- Example: Transaction Ledger (stdin lines → two dicts, then sort-and-print)

### Streaming ingestion / protocol framing
Data arrives as arbitrary chunks whose boundaries don't align with record boundaries. Buffer
partial input across calls, frame on the protocol's guaranteed delimiter, validate completeness.
- Example: SWE Open Call — `StreamingJsonlParser`; frame on `\n`, validate each line with
  `json.loads`, skip malformed lines, return raw record strings
- **The trap:** matching structure (first `{` … first `}`) instead of the frame. Fails on
  scalars (`true`, `42`), braces inside strings, and nested objects.
- **The fix:** buffer + delimiter + `json.loads` completeness check. Don't hand-roll a
  brace/string/escape state machine when framing + a stdlib parser does it.
- Contrast with stream aggregation: there whole events arrive intact; here a record can be
  split across chunks, so buffering partial input is the whole challenge.
- Generalizes to: length-prefixed / delimited protocols, log parsers, SSE/websocket consumers.

### Multiset / frequency-map
Check if a request can be satisfied by a pool of resources with per-item quantities.
- Example: Spell Check — letter availability per word, checked with Counter subtraction
- Key tool: `Counter(word) - Counter(available)` is empty `{}` iff all letters are available
- Generalizes to: anagram detection, inventory checks, resource allocation with limits

### Tree construction from flat input
Flat list of paths or call sequences → hierarchical tree with aggregated counts.
- Example: Stack trace profiler — natural structure: tree node with ordered-dict children

### Grid simulation
2D grid with entities and movement rules. Determine valid moves at each step.
- Example: Block puzzle — natural structure: grid (list of strings); cells as (row, col) tuples

### Datetime interval overlap
Events have start and end times. Naive equality check misses multi-day spans.
- Example: Trailer yard filter — use interval overlap formula, treat null exit as ∞

### Concurrent writes to denormalized state
Two tables must stay in sync under simultaneous requests. Naive read-modify-write produces lost updates.
- Example: Mosaic bookstore — `num_total_awards` must reflect every book increment atomically
- Three strategies: atomic SQL (no read needed), pessimistic lock (`SELECT FOR UPDATE`), optimistic lock (version column + retry)
- **This is a known weak spot.** Candidates who haven't explicitly studied this reach for wrong answers. Interviewers treat it as a strong signal.
- Correct pick here: atomic SQL inside one transaction — no read required, minimal lock scope.

### List deduplication with order preservation
A list contains duplicate values; the output must retain unique values in original order.
- Example: Axle — keep-first (`[0,1,2,0,3,0]` → `[0,1,2,3]`) and keep-last (`[0,1,2,0,3,0]` → `[1,2,3,0]`)
- Natural tool: `seen = set()` for O(1) membership; iterate forward (keep first) or backward then reverse (keep last)
- Key question: "which occurrence do you keep?" Interviewers may flip this after the first implementation.

### Async fan-out with per-item secondary fetch (React)
A primary API returns a list; some items have a foreign key ID that resolves via a second API.
Enrichment is optional — the item renders without it; include it only when the lookup succeeds.
- Example: M.AI L3 — fetch task list, then `Promise.all` over tasks with `assignedUser` to fetch user names; omit `card__owner` span on 404
- Pattern: `useEffect` → fetch primary → `Promise.all(items.map(async item => { ... }))` → `setState`
- 404 handling: check `res.ok`, return the un-enriched item rather than throwing
- Test surface: CSS class name presence/absence (`card__owner` span), not React state

### Controlled form + state lifting (React)
A form creates items that must immediately appear in a sibling list component. Both share
the same underlying collection — state must live in the common ancestor.
- Example: M.AI L2 — `CreateTaskForm` pushes to `todoItems`; `TaskColumn` renders it; both are children of `App`
- Validation: check required fields on submit, `return` early if invalid; do not clear fields on failed submit
- ID: generate with `uuidv4()` at submission time

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
- Letter needed more times than available (spell check)
- Input whitespace after comma-delimited fields (any stdin problem)

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
