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
naming conventions in CLAUDE.md. Output: `{NN}-prompt.md`, `{NN}-solution.md`,
and optionally `{NN}-solution.{ext}` for runnable code.

## What This File Is NOT
- Not a problem generator — it documents what actually happened in a real interview
- Not a pattern analyzer — that is `interview-repo-analyze`
- Not a skill gap evaluator — that is `skill-gap-analysis`

---

## Step 1: Identify the Session Directory

Convention: `YYMMDD-Company-Stack` (CamelCase, no spaces). If it doesn't exist,
ask for date, company, and stack. Do not create subdirectories.

## Step 2: Determine Problem Number

Find the highest existing `NN`. New problem is `NN + 1`, zero-padded. Start at `01`
if directory is empty.

## Step 3: Analyze the Raw Materials

Extract: problem statement (verbatim where possible), explicit constraints, progressive
phases, input/output format, examples. Ask if unclear: language, number of phases,
whether a class skeleton was given, what the interviewer said afterward. Do not infer
unstated constraints.

## Step 4: Write `{NN}-prompt.md`

Sections: title, source/date/stack/type, problem statement, requirements (labeled
Phase 1/2/3 if progressive), constraints, examples. Type field:
`Algorithmic | OOP | System Design | Full-stack | SQL | Mixed`.

## Step 5: Write `{NN}-solution.md`

Sections: approach (core insight, 2–4 sentences), phase breakdown (what changed and
why per phase), key decisions (non-obvious design choices), edge cases, complexity
(time + space), what this tests (1–2 sentences).

## Step 6: Write `{NN}-solution.{ext}` (if applicable)

For algorithmic and OOP problems: clean implementation of all phases, all edge cases,
minimal driver at bottom showing correct output. No TODOs, no debug artifacts.
Skip for system design and full-stack take-homes.

## Step 7: Route to Practice Repo

Based on the Type field:

| Type | Practice repo | Action |
|---|---|---|
| Algorithmic, OOP, Python | `/Users/eric/projects/SentryEval` | Check skill coverage |
| Full-stack, React, Node, TypeScript, SQL | `/Users/eric/projects/learn-react` | Check scenario/session coverage |
| System Design | No action — disconnected system | |

For SentryEval: read its `CLAUDE.md` and relevant skill files. Flag if the problem
type is not covered by an existing skill.

For learn-react: read its `CLAUDE.md`. Flag if the problem introduces a pattern not
covered by existing scenarios or the session generator.

If the stack is ambiguous, ask: "Should this map to SentryEval (Python/algorithmic)
or learn-react (Node/React/SQL)?"

## Step 8: Confirm Output

Report: directory, files created, one-sentence problem summary, practice repo
routing decision. Do not update `CLAUDE.md` — that is the user's responsibility.
