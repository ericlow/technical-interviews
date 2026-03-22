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
