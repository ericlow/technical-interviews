---
name: interview-repo-analyze
description: >
  Scan all interview session directories in this repository, extract algorithmic
  patterns, phase structures, and data structure usage, then write or refresh
  the _meta/ analysis files. Use when the repo has grown (new sessions added)
  and the analysis files are stale, or when starting a new session and wanting
  to reload current patterns into context. Triggers on "analyze the repo",
  "refresh the meta files", "update the pattern analysis", or "what patterns
  have you seen across all problems".
---

# Interview Repo Analyzer

## What This File Is
Reads all `{NN}-prompt.md` and `{NN}-solution.md` files and refreshes `_meta/`.

## What This File Is NOT
- Not a problem generator — analyzes existing problems, not new ones
- Not a skill evaluator — that is `skill-gap-analysis`
- Not a capture tool — that is `interview-capture`

---

## Step 1: Load Session Index

Read `CLAUDE.md` for the directory list. Do not scan the filesystem. If a session
was recently added, confirm `CLAUDE.md` is updated first.

## Step 2: Read All Problems

For each directory: read every `{NN}-prompt.md` (type, language, phases, operations)
and `{NN}-solution.md` (data structures, decisions, edge cases, what it tests).
Skip directories with no prompt files; note them as uncaptured.

## Step 3: Extract Patterns

- **Algorithmic patterns:** group by shape (command dispatch, OOP simulation, stream
  aggregation, tree construction, grid simulation, interval overlap, other). Per shape:
  which sessions, natural data structure.
- **Phase structure:** per problem, which phases were reached (1–4) and the scope ceiling.
- **Data structure usage:** per structure, which problems, and *why* it was the right choice.
- **Edge case taxonomy:** group across all problems by category (duplicate ops, invalid
  addressing, self-referential, capacity, null fields, boundary, string normalization).

## Step 4–6: Refresh `_meta/` Files

Overwrite all three files. Follow existing structure; update source date; add new
patterns found; remove patterns no longer supported by the session set.

- `analysis-patterns.md` — patterns table + per-pattern description and examples
- `analysis-phases.md` — phase framework table, per-phase examples, generation template
- `what-to-expect-algorithmic-interviews.md` — synthesis doc: format, evaluator intent,
  hidden test, phase structure, problem shapes, patterns, greedy reasoning, data structure
  rationale, edge case sourcing, extensibility principle

## Step 7: Append to `_meta/analysis-log.md`

Append-only. One entry per run with: sessions analyzed, sessions added since last run,
what changed per file, what prompted the change, and a narrative paragraph on how
understanding evolved. Never overwrite; never skip the narrative paragraph.

Create the file with a header if it does not exist.

## Step 8: Flag Practice Repo Impact

- **New Python/algorithmic/OOP patterns found** → flag: consider running `/skill-gap-analysis`
  against SentryEval (`/Users/eric/projects/SentryEval`)
- **New Node/TypeScript/React/SQL patterns found** → flag: consider extending learn-react
  scenarios or session generator (`/Users/eric/projects/learn-react`)
- **System design patterns** → note in analysis; no practice repo action needed
- **No new patterns** → state explicitly; no action needed in either repo

## Step 9: Confirm Output

Report: three files updated, log entry appended, session count, skipped sessions,
new patterns added, practice repo impact assessment.
