---
name: interview-capture
description: >
  Analyze raw interview materials (photos, PDFs, code files, notes) and generate
  standardized prompt/solution markdown files in the correct session directory.
  Use when the user wants to add a new interview session to the knowledge base,
  or when raw materials exist but no prompt/solution files have been written yet.
  Triggers on "capture this interview", "add this to the repo", "analyze these
  materials", or when the user drops files and asks what to do with them.
---

# Interview Capture Skill

## What This File Is
Converts raw interview materials into standardized markdown files following the
naming conventions defined in CLAUDE.md. Output is always `{NN}-prompt.md` and
`{NN}-solution.md` (and optionally `{NN}-solution.{ext}` for runnable code).

## What This File Is NOT
- Not a problem generator — it documents what actually happened in a real interview
- Not a pattern analyzer — that is `interview-repo-analyze`
- Not a skill gap evaluator — that is `skill-gap-analysis`

---

## Step 1: Identify the Session Directory

Check whether a directory already exists for this interview session.

**Directory naming convention:** `YYMMDD-Company-Stack`

- `YYMMDD` — date of the interview (zero-padded month and day)
- `Company` — company name, CamelCase, no spaces
- `Stack` — primary technology stack, CamelCase, no spaces or hyphens between technologies

**Examples:** `260130-Sentry`, `260320-Typescript-Node-React-Database`, `251014-AWS-manager`

If the directory does not exist, ask the user for:
1. The interview date
2. The company name
3. The primary stack

Create the directory. Do not create subdirectories inside it.

---

## Step 2: Determine the Problem Number

List existing files in the directory. Find the highest `NN` already present.
The new problem is `NN + 1`, zero-padded to two digits (01, 02, 03...).

If the directory is empty, start at `01`.

---

## Step 3: Analyze the Raw Materials

Examine all provided materials: photos, PDFs, code files, notes, descriptions.

**Extract:**
- The problem statement as given (not paraphrased — preserve the actual ask)
- Any constraints stated explicitly (time, memory, API shape)
- The progressive phases if multiple requirements were given
- The expected input/output format
- Any example cases shown

**Ask the user if unclear:**
- What language was used or expected?
- Were there multiple phases or just one?
- Was there a class skeleton or interface given upfront?
- What did the interviewer say after the candidate's solution?

Do not infer constraints that were not stated. Prefer quoting verbatim over paraphrasing when the original wording is available.

---

## Step 4: Write `{NN}-prompt.md`

The prompt file documents what was asked — not the solution.

### Format

```markdown
# [Problem Title]

**Source:** [Company], [Date]
**Stack:** [Language / framework]
**Type:** [Algorithmic | OOP | System Design | Full-stack | SQL | Mixed]

---

## Problem Statement

[Verbatim or close-paraphrase of the problem as given. Preserve the original
framing. If a class skeleton was provided, include it here as a code block.]

## Requirements

[Bulleted list of explicit requirements, in the order they were introduced.
If requirements were added progressively, label them Phase 1 / Phase 2 etc.]

## Constraints

[Any stated constraints: time limit, input size, API boundaries, etc.]

## Examples

[Any example inputs/outputs shown during the interview.]
```

---

## Step 5: Write `{NN}-solution.md`

The solution file documents the approach, reasoning, and tradeoffs — not just
the code. This is what future sessions load to understand how to solve this
class of problem.

### Format

```markdown
# [Problem Title] — Solution

## Approach

[2–4 sentences: what is the core insight? What data structure or pattern
does this problem reduce to?]

## Phase Breakdown

### Phase 1 — [Name]
[What the phase requires. What data structure is used. Why.]

### Phase 2 — [Name]
[What changed. What new lookup or search was introduced. Why.]

### Phase 3 — [Name] (if applicable)
[What optimization was added. What metric is being minimized/maximized.]

## Key Decisions

[Bulleted list of non-obvious design choices: where state lives, what structure
to use for the secondary lookup, return type consistency, etc.]

## Edge Cases

[Bulleted list of domain-specific edge cases: what can go wrong, what the
correct behavior is.]

## Complexity

- Time: [per-operation complexity]
- Space: [total space for the data structures used]

## What This Tests

[1–2 sentences: what skill is the interviewer actually evaluating?]
```

---

## Step 6: Write `{NN}-solution.{ext}` (if applicable)

If the problem has a runnable solution (algorithmic or OOP problems), write
clean Python (or the interview language) that:

- Implements all phases
- Handles all edge cases documented in the solution file
- Includes a minimal driver at the bottom that demonstrates correct output
- Has no debugging artifacts, no TODOs, no placeholder comments

System design and full-stack take-home problems do not require a runnable file.

---

## Step 7: Route to Practice Repo

After capturing the problem, determine whether a practice repo should be updated
or checked for coverage. Use the problem type from the `{NN}-prompt.md` Type field:

| Problem type | Practice repo | Action |
|---|---|---|
| Algorithmic, OOP, Python | `/Users/eric/projects/SentryEval` | See routing below |
| Full-stack, React, Node, TypeScript, SQL | `/Users/eric/projects/learn-react` | See routing below |
| System Design | No action — handled by a separate disconnected system |

**If Python / Algorithmic / OOP:**
Read `/Users/eric/projects/SentryEval/CLAUDE.md` and the relevant skill files
(`oop-problem-gen`, `applied-oop-problem-gen`, `algo-problem-gen`). Ask:
does the newly captured problem fit a problem type that is already covered by
an existing skill? If yes, confirm coverage. If no, flag it:
> "This problem type is not covered by any current SentryEval skill. Consider
> running `/skill-gap-analysis` to evaluate whether a new skill is needed."

**If Node / TypeScript / React / SQL:**
Read `/Users/eric/projects/learn-react/CLAUDE.md`. Ask: does the problem fit
an existing scenario or session type? If the problem introduces a new pattern
not covered by any scenario or the session generation system, flag it:
> "This problem type may not be covered by the current learn-react scenarios.
> Consider adding a scenario or extending the session problem generator."

**If uncertain about routing**, ask the user: "This problem used [stack] —
should this map to SentryEval (Python/algorithmic) or learn-react (Node/React/SQL)?"

---

## Step 8: Confirm Output

After writing the files, report:
- The directory name
- The files created (with full paths)
- A one-sentence summary of the problem for the user to verify accuracy
- The practice repo routing decision (or "System Design — no action")

Do not update CLAUDE.md — that is the user's responsibility when adding a new
session directory to the table.
