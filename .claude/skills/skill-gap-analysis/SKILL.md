---
name: skill-gap-analysis
description: >
  Compare existing problem-generation skills in a coaching framework (e.g.
  SentryEval) against the patterns observed in the historical interview repository.
  Identify mismatches, missing problem types, and calibration errors. Produces
  a gap report with specific recommendations. Use when the user wants to know
  whether their practice system reflects real interview patterns, or before
  writing a new skill. Triggers on "analyze my skills", "do my skills match
  real interviews", "what's missing from my practice system", or "evaluate
  the skill against historical problems".
---

# Skill Gap Analyzer

## What This File Is
A meta-skill that evaluates whether an existing coaching skill accurately
reflects the patterns observed in real interviews captured in this repository.
Output is a gap report and a recommendation for what to build, change, or drop.

## What This File Is NOT
- Not a problem generator
- Not a skill writer — it identifies gaps; writing the skill is a separate step
- Not a repo analyzer — load `interview-repo-analyze` first if `_meta/` is stale

---

## Step 1: Load Historical Patterns

Read the three `_meta/` files:
- `_meta/analysis-patterns.md` — algorithmic patterns and data structure usage
- `_meta/analysis-phases.md` — phase structure across all problems
- `_meta/what-to-expect-algorithmic-interviews.md` — full synthesis

If these files are older than the most recent session directory (check CLAUDE.md),
warn the user and recommend running `interview-repo-analyze` first.

---

## Step 2: Identify Which Practice Repo to Evaluate

There are two practice repos. The correct one depends on what the user wants to evaluate:

| Repo | Path | When to use |
|---|---|---|
| **SentryEval** | `/Users/eric/projects/SentryEval` | Python-based algorithmic, OOP, or applied OOP problems |
| **learn-react** | `/Users/eric/projects/learn-react` | Node / TypeScript / React / SQL full-stack problems |
| **System design** | N/A — disconnected system | Do not evaluate — no skills here to assess |

If the user did not specify which repo, ask:
> "Are you evaluating SentryEval (Python/algorithmic) or learn-react (Node/React/SQL)?"

Read the target repo's `CLAUDE.md` first to understand what skills exist, then
read the relevant `SKILL.md` files.

**For SentryEval**, the skills to consider are:
- `/Users/eric/projects/SentryEval/.claude/skills/oop-problem-gen/SKILL.md`
- `/Users/eric/projects/SentryEval/.claude/skills/applied-oop-problem-gen/SKILL.md`
- `/Users/eric/projects/SentryEval/.claude/skills/algo-problem-gen/SKILL.md`

**For learn-react**, the skills to consider are:
- `/Users/eric/projects/learn-react/.claude/skills/start-session/SKILL.md`
- `/Users/eric/projects/learn-react/.claude/skills/end-session/SKILL.md`
- `/Users/eric/projects/learn-react/.claude/skills/scenario-practice/SKILL.md`

Read the full `SKILL.md` for each skill being evaluated. Extract:
- What problem type does it claim to generate or run?
- What phase structure does it follow?
- What data structures or patterns does it target?
- What validation tests does it apply?
- What domains does it cover / exclude?
- What is the ceiling on complexity (what is explicitly out of scope)?

---

## Step 3: Compare Against Historical Patterns

For each skill, evaluate on five dimensions:

### 3.1 Phase Structure Match
Does the skill's phase progression match the observed pattern?
- Phase 1: direct operation with given addressing (no search, no optimization)
- Phase 2: automate the search (data structure choice becomes meaningful)
- Phase 3: optimize with a metric (correctness is no longer enough)

**Mismatch signals:**
- Phase 1 requires search or optimization that real Phase 1 never requires
- Phase 2 is identical to Phase 1 (no structural escalation)
- Phase 3 complexity ceiling is too high (heaps, rate limiting) or too low (trivial sort)

### 3.2 Interface Convention Match
Does the skill match how problems are actually presented in interviews?
- Applied OOP problems: interface/skeleton given upfront
- Open-ended design: candidate discovers entities through questions
- Algorithmic: input/output spec given, no class skeleton

**Mismatch signal:** Skill uses open-ended discovery for problems where
historical interviews provided a skeleton.

### 3.3 Validation Tests Match
Does the skill's difficulty validation catch the problems that real candidates
fail at?
- The primary test for OOP: extensibility — does a naive Phase 1 break under Phase 2?
- Secondary tests: state storage decision, business logic decision, Phase 3 metric clarity

**Mismatch signal:** Validation tests target sophistication metrics (bidirectional
references, multiple inheritance) that don't appear in historical problems.

### 3.4 Domain Coverage Match
Do the skill's example domains produce problems of the right shape and complexity?
- Applied OOP domains (from historical record): parking, banking, library, ride-share, logistics
- Algorithmic domains: word frequency, grid puzzles, datetime intervals, tree construction
- Out of scope for applied OOP: domains that require heaps or real-time rate limiting

**Mismatch signal:** Skill includes domains that require sophisticated data
structures the historical problems never reached.

### 3.5 Complexity Ceiling Match
Is the maximum complexity the skill can generate calibrated to the 60-minute
interview format?
- Applied OOP ceiling: linear scan + min/max + tiebreaker
- Algorithmic ceiling (Phase 3): O(n log n) sort, BFS, simple DP
- Above ceiling: persistent data structures, segment trees, distributed coordination

**Mismatch signal:** Skill can generate problems that no 60-minute session
in this repo ever reached.

---

## Step 4: Produce the Gap Report

### Format

```markdown
# Skill Gap Report: [Skill Name]

**Evaluated:** [Date]
**Against:** _meta/ files dated [Date]

## Summary
[2–3 sentence verdict: is this skill well-calibrated, partially mismatched, or wrong?]

## What the Skill Gets Right
- [Specific things that match historical patterns]

## Gaps Identified

### Gap 1: [Name]
**Dimension:** [Phase Structure | Interface Convention | Validation | Domain | Complexity]
**Observed in history:** [What the historical record shows]
**What the skill does:** [How the skill differs]
**Impact:** [How this affects the quality of generated problems]
**Recommendation:** [Specific change or new skill to write]

[Repeat for each gap]

## Recommendation
[One of: "skill is well-calibrated", "update skill — specific changes listed above",
"write a new skill — existing skill covers a different use case",
"deprecate skill — historical record does not support this problem type"]
```

---

## Step 5: Recommend Next Action

Based on the gap report, recommend exactly one of:

1. **No action** — skill matches historical patterns; no changes needed
2. **Update the skill** — specific gaps are fixable by editing the existing SKILL.md
3. **Write a complementary skill** — existing skill is correct for one use case,
   but a different use case observed in history is uncovered (e.g., `oop-problem-gen`
   covers FAANG-style; `applied-oop-problem-gen` covers interface-first)
4. **Deprecate the skill** — the problem type it generates does not appear in
   the historical record and is unlikely to appear in future interviews

If the recommendation is (2) or (3), offer to proceed immediately.
