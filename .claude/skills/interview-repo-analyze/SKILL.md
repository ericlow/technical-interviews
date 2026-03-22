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
Reads all `{NN}-prompt.md` and `{NN}-solution.md` files across every session
directory and produces or refreshes the three analysis files in `_meta/`.

## What This File Is NOT
- Not a problem generator — it analyzes existing problems, not new ones
- Not a skill evaluator — that is `skill-gap-analysis`
- Not a capture tool — that is `interview-capture`

---

## Step 1: Load the Session Index

Read `CLAUDE.md` to get the current list of session directories. Do not scan
the filesystem for directories — trust the index. If the user says a session
was added recently, ask them to confirm CLAUDE.md has been updated first.

---

## Step 2: Read All Problems

For each directory in the index:
1. Read every `{NN}-prompt.md` — extract: problem type, language, phase structure,
   core operation, input/output shape
2. Read every `{NN}-solution.md` — extract: data structures used, key design
   decisions, edge cases, what the problem tests

Do not read raw source files (PDFs, images, original code) — only the generated
markdown files. If a session directory has no `{NN}-prompt.md` files, skip it
and note it as uncaptured.

---

## Step 3: Extract Patterns

From the full set of problems, identify and document:

### Algorithmic patterns
Group problems by shape:
- Command dispatch (route by type, validate, mutate)
- OOP simulation with progressive requirements
- Stream aggregation (running aggregate + query)
- Tree construction from flat input
- Grid simulation
- Datetime interval overlap
- Other

For each shape: which sessions exhibit it, what data structure it naturally maps to.

### Phase structure
For each problem, document which phases were present:
- Phase 1: direct operation, caller provides addressing
- Phase 2: automate the search
- Phase 3: optimize with a metric
- Phase 4: scale / distribution

Note which problems only reached Phase 1 or 2 (scope ceiling for that interview).

### Data structure usage
For each data structure (dict, list, tree, grid, heap, set): which problems used
it, and *why* — what lookup or operation made it the right choice.

### Edge case taxonomy
Group edge cases by category across all problems:
- Duplicate operations (already parked, account exists)
- Invalid addressing (not found)
- Self-referential (same-account transfer)
- Capacity / empty (no available spots)
- Null fields (trailer still present)
- Boundary (exact balance, exactly at capacity)
- String normalization (punctuation, case)

---

## Step 4: Write `_meta/analysis-patterns.md`

Overwrite the file. Format:

```markdown
# Analysis: Algorithmic Patterns Observed

## Source
Derived from analysis of all interview sessions in this repository ([Month Year]).

## Problems classified as algorithmic

| Session | Problem | Language |
...

## Pattern 1: [Name]
[Description, examples, practice implication]

...
```

Follow the structure of the existing file. Update the source date. Add new
patterns if found. Remove patterns that no longer appear after re-analysis.

---

## Step 5: Write `_meta/analysis-phases.md`

Overwrite the file. Format: phase framework table, per-phase examples drawn
from the current set of problems, practical generation template at the end.

Update examples to reflect the current session list — do not leave references
to sessions that no longer exist or have been renamed.

---

## Step 6: Write `_meta/what-to-expect-algorithmic-interviews.md`

Overwrite the file. This is the synthesis document — designed to be loaded into
context at the start of a practice session to prime the LLM.

Sections (preserve structure, refresh content):
1. Format (session length, number of problems, expectations)
2. What interviewers are actually evaluating
3. The hidden test (extensibility)
4. Phase structure table
5. Problem shapes and natural data structures
6. Algorithmic patterns (with examples from current sessions)
7. Greedy reasoning (when safe, when not, what to say)
8. What interviewers ask about data structures
9. Edge cases always come from the domain
10. The extensibility principle (signs Phase 1 will break vs. hold)

---

## Step 7: Confirm Output

Report:
- The three files updated with their paths
- Count of sessions analyzed
- Any sessions skipped (no prompt/solution files)
- Any new patterns added vs. the previous version
- The date used in the "Source" line (today's date)
