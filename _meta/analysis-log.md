# Analysis Log

A dated record of how the meta-analysis files have evolved. Each entry documents
what changed, what prompted the change, and what new understanding it reflects.
Load this file when you want to understand how thinking about the problem domain
has developed over time, not just the current state.

---

## 2026-03-21

**Sessions analyzed:** 12
**Sessions added since last run:** All (initial analysis)

### What changed

This is the founding entry. All three analysis files were created from scratch
by analyzing every session directory in the repository.

**analysis-patterns.md** — Created. Documents 7 patterns extracted from the
full session set: progressive requirements, when to reach for a dict, data shape
selection, greedy reasoning, string normalization, interval overlap, and
real-world framing. Each pattern is grounded in specific session examples.

**analysis-phases.md** — Created. Documents the Phase 1–4 framework observed
across all sessions. Corrects the "CRUD is Phase 1" misconception — the defining
characteristic is not the operation type but the simplicity of assumptions
(no search, no optimization). Includes a practical problem generation template.

**what-to-expect-algorithmic-interviews.md** — Created. Full synthesis document
covering format, what interviewers evaluate, the hidden test (extensibility),
phase structure, problem shapes, algorithmic patterns, greedy reasoning,
data structure rationale, edge case sourcing, and the extensibility principle.
Designed to be loaded into context at the start of a practice session.

### What prompted the change

The repository was consolidated from raw interview materials (photos, PDFs,
code files, notes) spanning 12 sessions across companies including Sentry,
Everlaw, DoorDash, GrowTherapy, AWS, Supio, Baton, and Resfrac. Prior to this
analysis, no structured synthesis existed — each session directory contained
its own prompt/solution files but there was no cross-session pattern extraction.

The immediate trigger was evaluating whether an existing coaching skill
(`oop-problem-gen` in SentryEval) accurately reflected the interview patterns
in the historical record. Answering that question required first synthesizing
what those patterns actually were.

### How our understanding evolved

The most important insight from this initial analysis was the **extensibility
principle**: the real difficulty of interview problems is not Phase 1, it is
whether Phase 1 was written in a way that Phase 2 can bolt on without a
structural rewrite. This pattern appeared consistently across the OOP problems
(parking garage, bank account) and distinguished strong solutions from weak ones
more reliably than any other single factor.

A second key insight was the **interface convention distinction**: applied OOP
interviews (the Sentry parking garage, the bank account command dispatch) give
the candidate a class skeleton or interface upfront. Open-ended system design
interviews do not. These are fundamentally different problem formats that require
different coaching skills — but they had previously been conflated into a single
`oop-problem-gen` skill. This analysis directly motivated writing
`applied-oop-problem-gen` as a separate skill calibrated to the interface-first
pattern.

A third insight was the **phase ceiling observation**: no session in this
repository reached heap-level complexity in an OOP context. Phase 3 optimizations
were universally linear scan + `min()`/`max()` with a key function, sometimes
with a tiebreaker. Coaching skills that target heap-level complexity are
miscalibrated for the interview format represented here.

---

## 2026-03-21 (revision)

**Sessions analyzed:** 12
**Sessions added since last run:** None — correction to existing analysis

### What changed

**analysis-patterns.md** — Pattern 7 revised. The original claim ("no abstract
LeetCode — problems simulate actual systems") was imprecise. Replaced with a
two-sub-type distinction: *algorithmically-core* problems (tree construction,
greedy grid, stream aggregation) where the domain is a wrapper around a
recognizable CS algorithm; and *systems-core* problems (applied OOP, interval
logic) where the algorithm is trivial and the challenge is design and extensibility.

**what-to-expect-algorithmic-interviews.md** — Added a "Two problem types" section
before the pattern list. Reframed the opening question from "what pattern is this?"
to "is the hard part the algorithm, or the design?" Condensed the pattern
descriptions to make room without exceeding file size limits.

**analysis-log.md** — This entry.

### What prompted the change

Observation that the Sentry session asked both a tree construction problem (stack
trace profiler) and an applied OOP problem (parking garage) in the same interview.
The profiler is algorithmically-core — its core challenge is building a trie-like
structure from flat input, which is a recognizable CS problem type regardless of
the stack trace framing. Treating it the same as the parking garage (systems-core)
was a meaningful analytical error.

### How our understanding evolved

The original analysis overcorrected against LeetCode framing. "Real-world domain"
is true of every problem here, but it does not mean every problem is free of
algorithmic thinking. The more useful distinction is whether the difficulty lives
in the algorithm (recognize it, implement it) or in the design (extensibility,
state placement, OOP structure).

This matters for practice: algorithmically-core problems reward pattern recognition
and should be drilled in SentryEval with `algo-problem-gen`. Systems-core problems
reward design instincts and should be drilled with `applied-oop-problem-gen`. A
session that asks both — like the Sentry session — is testing two different skills
in sequence, and preparation should reflect that.

---

## 2026-03-26

**Sessions analyzed:** 13
**Sessions added since last run:** 1 — `260326-Python-HackerRank-TabaPay`
**Skipped (no prompt files):** `260322-Verkada` (prep_plan.md only — not yet capturable)

### What changed

**analysis-patterns.md** — Added `260326-Python-HackerRank-TabaPay` to the problems
table (2 new problems: Transaction Ledger and Spell Check). Added Pattern 8: Multiset /
frequency-map reasoning (Counter subtraction for availability checks). Updated Pattern 1
with an explicit note that automated screens do not follow the progressive requirements
pattern. Updated Pattern 7 to include the TabaPay problems as algorithmically-core examples.

**analysis-phases.md** — Added Transaction Ledger and Spell Check to the Phase 1
examples table. Added a note at the top distinguishing automated screens (HackerRank)
from live interviews: automated screens are always single-phase, pass/fail, no progressive
requirements.

**what-to-expect-algorithmic-interviews.md** — Updated Format section to distinguish
live interviews from automated screens. Added "multiset availability check" to the
problem shapes table. Added Multiset/frequency-map as a new pattern in the patterns
section. Added Spell Check and Transaction Ledger as examples under Stream Aggregation
and the new Multiset section. Added two new edge case examples (letter quantity
mismatch, input whitespace after commas).

**analysis-log.md** — This entry.

### What prompted the change

`260326-Python-HackerRank-TabaPay` appeared as an untracked directory with full
prompt/solution files. The session was a HackerRank automated screen with two
self-contained problems. This is the first automated-screen session in the repository —
all prior algorithmic sessions were live human-interviewer formats.

Note: CLAUDE.md does not yet list `260326-Python-HackerRank-TabaPay` or
`260322-Verkada`. Both should be added to the directory table.

### How our understanding evolved

The TabaPay session introduced the first example of **multiset reasoning** in the
repository — specifically the Spell Check problem, where the challenge is whether a
word's letter requirements can be satisfied by a pool with per-letter counts. This is
meaningfully different from the word counter (Everlaw), which aggregates frequencies
into a dict for querying. In spell check, the dict is compared against another dict,
not queried directly. The key tool is Counter subtraction, which handles the "not
enough of this letter" case that a set-membership check would miss.

The Transaction Ledger problem reinforced an existing sub-pattern (stdin parsing →
accumulation → sort-then-print) but added the detail that automated HackerRank problems
place heavy weight on exact output formatting — a dimension not tested in live interviews
where the interviewer can clarify ambiguities.

More broadly, the presence of an automated screen session clarifies that the phase
framework is a property of live interview format, not of algorithmic problems in general.
HackerRank problems are single-phase by design: there is no interviewer to extend the
requirements, so extensibility is not evaluated. This means SentryEval's progressive
problem generation is correctly calibrated for live sessions but should not be used to
practice for automated screens — those require a different drill focused on clean
single-problem execution and edge case enumeration.

---

## 2026-05-11

**Sessions analyzed:** 14 (15 directories total; 1 skipped)
**Sessions added since last run:** 1 — `260511-Mosaic-Python`
**Skipped (no prompt files):** `260322-Verkada` (prep materials only)

### What changed

**analysis-patterns.md** — Added `260511-Mosaic-Python` to a new "Take-home backend API sessions" table (separate from the algorithmic problems table, since the classification doesn't fit). Added Pattern 9: Concurrent writes to denormalized state — covering the lost update problem, and all three strategies (atomic SQL, pessimistic lock, optimistic lock) with explicit coaching guidance that candidates must reason through all three and pick one with justification.

**analysis-phases.md** — Added Mosaic bookstore to Phase 1 examples (CRUD endpoints) and Phase 4 examples (concurrent award increment discussion).

**what-to-expect-algorithmic-interviews.md** — Added a third format type (take-home backend API project) to the Format section. Added "two tables in sync, one denormalized" as a new problem shape. Added "Concurrent writes to denormalized state" as a new pattern in the patterns section with a coaching warning.

**analysis-log.md** — This entry.

### What prompted the change

`260511-Mosaic-Python` was captured from a Mosaic interview on 2026-05-11. The problem is a backend REST API take-home: 5 CRUD endpoints, an award-increment endpoint that updates two tables atomically, and stretch goals for soft deletes, genre aliasing, and filtering/pagination/sorting. The concurrency section — "what could go wrong if multiple requests hit this endpoint simultaneously?" — is the primary evaluative signal in the interview.

### How our understanding evolved

This session introduced two things the repository had not seen before. First, a **third interview format**: the take-home backend API project. Prior sessions were either live human-interviewer algorithmic problems (with progressive requirements) or automated HackerRank screens (single-phase, pass/fail). The Mosaic format is different from both — it gives the candidate full stack ownership, uses stretch goals instead of live phase escalation, and explicitly tests concurrency and schema design.

Second, and more significantly, it introduced the **lost update / concurrent write pattern** as a distinct interview topic. This is qualitatively different from prior concurrency content in the repository (which appeared only in Phase 4 discussions about scale). Here, concurrency is a first-class engineering question: the candidate must know why naive read-modify-write fails, and must be able to articulate when to use atomic SQL vs. `SELECT FOR UPDATE` vs. optimistic locking with a version column. The distinction is not trivia — it reflects whether the candidate has actually reasoned about database behavior under load, or is just hoping the ORM handles it.

This is flagged as a **known weak spot** in the coaching notes because ORMs abstract it away in day-to-day work. Candidates who haven't explicitly studied it will either say nothing or propose application-level solutions (mutexes, locks in code) that don't work across multiple web server processes. Any practice problem generated from this pattern must require the candidate to name all three strategies and defend their choice.

---

## 2026-05-20

**Sessions analyzed:** 16 (16 directories total; 1 skipped)
**Sessions added since last run:** 1 — `260520-Axle`
**Skipped (no prompt files):** `260322-Verkada` (prep materials only)

### What changed

**analysis-patterns.md** — Added `260520-Axle` in a new "Fundamentals / fluency screens" table, separate from the algorithmic and take-home tables. Added a note under Pattern 2 about dict merge with collision handling, specifically the anti-pattern of mutating an input dict (observed in the interview solution's own docstring). Added Pattern 10: List deduplication with order preservation — covering keep-first (forward pass with seen-set) vs. keep-last (reverse, apply keep-first, reverse result).

**analysis-phases.md** — Added a note distinguishing the fundamentals/fluency screen format from automated HackerRank screens. Added Axle's four exercises to the Phase 1 examples table. This is the first session in the repository where *all* exercises are Phase 1 only — no escalation occurs.

**what-to-expect-algorithmic-interviews.md** — Added "Fundamentals / fluency screen" as a fourth format type in the Format section. Added "ordered list with duplicates — keep first or last" as a new problem shape. Added "List deduplication with order preservation" as a new pattern in the patterns section.

**analysis-log.md** — This entry.

### What prompted the change

`260520-Axle` was captured from an Axle interview on 2026-05-20. The session consisted of 4 short Python exercises — a divisible filter (with parameterization), dict merge with collision summing, and two deduplication variants (keep-first and keep-last). None of the exercises escalated past Phase 1.

### How our understanding evolved

This session introduced a **fourth interview format**: the fundamentals / fluency screen. It is distinct from the three previously documented formats in a meaningful way. Live algorithmic screens test problem-solving and extensibility over one or two complex problems. Automated HackerRank screens test correctness and edge case coverage over self-contained problems. Take-home backend projects test full-stack reasoning. The Axle format does none of these — it tests whether the candidate can write basic Python correctly and quickly, across several small exercises with no design decisions required.

The practical implication is that this format is **best prepared for with mechanical drills**, not with SentryEval's problem generators. The `mechanical-drills` skill in SentryEval already covers the relevant categories: `list-comp` (divisible filter), `sets` (deduplication with seen-set), and dict operations (merge with collision). The dict-merge exercise maps closest to `defaultdict` accumulation patterns but is not exactly covered — `defaultdict` targets single-dict accumulation, while the Axle exercise tests merging *two* dicts with a specified collision strategy. This is a small gap worth noting.

The deduplication keep-last variant is new to the repository and is notable because it tests **traversal direction reasoning** — a candidate who only knows the forward-pass pattern must think carefully about how to adapt it. This is a good single-mechanic drill: trivial in scope but requires explicit reasoning about iteration order.

---

## 2026-06-03 — Admin: SentryEval deprecated, replaced by learn-python

**Sessions analyzed:** 0 — no new sessions  
**Sessions added since last run:** None

### What changed

All references to `SentryEval` (`/Users/eric/projects/SentryEval`) across this
repository have been updated to `learn-python` (`/Users/eric/projects/learn-python`).
Affected files: `CLAUDE.md`, `_meta/analysis-log.md`, and all three skill files
(`interview-capture`, `interview-repo-analyze`, `skill-gap-analysis`).

`SentryEval` has been deprecated. Its functionality — `oop-problem-gen`,
`applied-oop-problem-gen`, `algo-problem-gen`, `interview-coach`, `session-review`,
`mechanical-drills` — has been relocated to `learn-python`, which also adds
`db-problem-gen`, `db-interview-coach`, and `db-session-review`.

Historical log entries that mention `SentryEval` by name are intentionally preserved
as-is — they accurately reflect the state of the system at the time they were written.

---

## 2026-06-12

**Sessions analyzed:** 17 (17 directories total; 1 skipped)
**Sessions added since last run:** 1 — `260611 - M.AI-React.AI`
**Skipped (no prompt files):** `260322-Verkada` (prep materials only)

### What changed

**analysis-patterns.md** — Added a new "UI / front-end screens" table alongside the
existing algorithmic and take-home tables, covering `240903-FrontEnd-React` and
`260611 - M.AI-React.AI`. Added Pattern 11: Async fan-out with per-item secondary fetch
(React) — `useEffect` + `Promise.all` + conditional enrichment with 404 tolerance.
Added Pattern 12: Controlled form + state lifting — form creates items that appear
immediately in a sibling component via shared parent state. Updated source date.

**analysis-phases.md** — Added a fourth automated format note: Progressive UI screens
(CodeSignal), distinct from HackerRank — levels unlock sequentially, DOM-queried via
CSS selectors, phase ceiling is Phase 2. Added M.AI L1 and L2 to Phase 1 examples;
added M.AI L3 and L4 to Phase 2 examples. Updated source date.

**what-to-expect-algorithmic-interviews.md** — Added "Progressive UI screen (CodeSignal)"
as a fifth format type in the Format section. Added two new problem shapes to the shapes
table: (1) list of items with optional FK enrichment from secondary API, and (2) user
creates items that appear immediately in a sibling component. Added two new patterns
at the end of the patterns section: Async fan-out with per-item secondary fetch, and
Controlled form + state lifting. Updated source date.

**analysis-log.md** — This entry.

### What prompted the change

`260611 - M.AI-React.AI` was captured from an M.AI CodeSignal assessment on 2026-06-11.
The problem was a 4-level progressive Kanban board (task management system) in React and
TypeScript. Levels unlocked sequentially by passing an automated test suite that queried
the DOM via CSS selectors. Levels 1–3 were completed within 90 minutes; Level 4 was not
reached.

### How our understanding evolved

This session introduced the **fifth distinct interview format** in the repository: the
progressive UI screen. It is categorically different from all four previously documented
formats. Unlike HackerRank (algorithmic, pass/fail), it tests front-end architecture and
async fluency. Unlike a live interview (progressive requirements via human escalation),
the progression is automated and locked — you cannot skip or negotiate. Unlike a take-home
(open stack, full ownership), the scaffold and class names are given. Unlike a fluency
screen (Phase 1 only), it escalates to Phase 2 at L3 via async data fetching.

The most analytically interesting aspect is the **test surface**: tests do not inspect
React state, hooks, or component internals — they query the rendered DOM using BEM class
names. This means spec fidelity (using `card__title`, `column__cards`, `card__owner`
exactly as specified) is not a style preference; it is the mechanism by which passing
or failing is determined. A candidate who doesn't notice the class names are fixed will
fail tests that their logic would otherwise satisfy.

The L3 pattern — fetch a flat list, then fan out per-item to a secondary API, merge
optional enrichment, render with conditional display — is the most transferable new
pattern from this session. It is a front-end analog to the backend "concurrent fan-out
with partial failure tolerance" pattern first observed in the AWS manager session. Both
use `Promise.all` with per-item error suppression; the difference is that the React
version's failure condition is a 404 on a secondary call rather than a regional AWS API
timeout. The right response in both cases is to return the un-enriched result rather than
failing the whole request.

This session also reinforces that the Phase 1–4 framework applies across domains — not
only to algorithmic backend problems. L1–2 are unambiguously Phase 1 (data given, render
it; user action given, handle it). L3 is Phase 2 (go find the data yourself). The
framework holds even when the "algorithm" is a React render cycle.

---

## 2026-09-18

**Sessions analyzed:** 19 (19 directories total; 1 skipped)
**Sessions added since last run:** 2 — `260729-Blue-Shield`, `260917-SWE-OpenCall`
**Skipped (no prompt files):** `260322-Verkada` (prep materials only)

### What changed

**analysis-patterns.md** — Added `260917-SWE-OpenCall` to the automated-screen problems
table. Added a new "System design sessions" table (GrowTherapy, DoorDash, Supio, and both
Blue Shield problems) for completeness — these had never been tracked in the patterns file.
Added Pattern 13: Streaming ingestion — framing arbitrary chunks into records. Updated source
date.

**analysis-phases.md** — Added a note distinguishing CodeSignal-style automated *coding*
screens (single stateful class, hidden-test escalation) from HackerRank and the CodeSignal
*UI* screen. Added the streaming parser to Phase 1 examples and Blue Shield to Phase 4
examples. Updated source date.

**what-to-expect-algorithmic-interviews.md** — Added "Automated coding screen with
hidden-test escalation" as a format. Added "stream of arbitrary chunks framed into records"
to the shapes table. Added a "Streaming ingestion / protocol framing" pattern, placed next to
stream aggregation to make the contrast explicit. Updated source date.

**analysis-log.md** — This entry.

### What prompted the change

Two untracked sessions were captured. `260729-Blue-Shield` is a verbal system-design
interview (e-commerce for 100k users: JWT/RBAC internals, async order flow, plus backend
domain probes on microservice chatter and resumable 1 TB upload). `260917-SWE-OpenCall` is a
CodeSignal-style Python coding screen: a single `StreamingJsonlParser` class graded on 16
hidden test cases with exact output.

### How our understanding evolved

The SWE Open Call session introduced the repository's first **streaming / protocol-framing**
problem, and it is genuinely new. Prior "stream" content (the Everlaw word counter, the
TabaPay transaction ledger) assumed whole events arrive intact — you aggregate discrete items.
Here the defining difficulty is the opposite: **record boundaries do not align with arrival
boundaries.** A single JSON value may be split across many `feed()` calls, and one call may
carry several values. The correct move is to buffer partial input and frame on the protocol's
guaranteed delimiter (the newline in JSONL), validating each framed segment with `json.loads`.
The seductive wrong move — matching the first `{` to the first `}` — fails on every non-trivial
case (scalars have no braces, strings can contain `}`, objects nest). The lesson worth drilling
is "frame the transport, don't parse the structure," plus "reach for the stdlib parser instead
of hand-rolling a brace/escape state machine."

This session also sharpened the taxonomy of automated screens. The repo already had HackerRank
(multiple self-contained problems) and the CodeSignal *UI* screen (DOM-queried, progressive
levels). SWE Open Call is a third automated variant: a CodeSignal-style *coding* screen built
around one stateful class, where the requirement escalation that a live interviewer would speak
aloud is instead hidden inside the test suite. The practical implication is that edge-case
enumeration must be proactive — the happy path passes nothing on its own, and "All test cases
failed" gives no diagnostic signal about which class of input broke.

Blue Shield contributed the repository's first explicitly-tracked system-design entries in the
patterns file. No practice-repo action follows from it (system design is a disconnected track),
but it reinforced that the Phase 4 lens — scale, concurrency, failure modes — describes verbal
architecture interviews as well as it describes the scale phase of a live coding problem.

### Practice repo impact

- **learn-python:** the streaming / protocol-framing pattern is new and likely uncovered by the
  existing algorithmic and `coderbyte-drill` generators (those parse a complete input in one
  shot; none maintain buffer state across incremental calls). Recommend running
  `/skill-gap-analysis` against learn-python to decide whether to add a streaming/stateful-parse
  drill.
- **learn-react:** no impact this run.
- **System design (Blue Shield):** noted in analysis only; no practice-repo action.
