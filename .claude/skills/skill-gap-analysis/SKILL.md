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
Evaluates whether a coaching skill accurately reflects patterns in this repo.
Output: gap report and recommendation.

## What This File Is NOT
- Not a skill writer — identifies gaps; writing is a separate step
- Not a repo analyzer — run `interview-repo-analyze` first if `_meta/` is stale

---

## Step 1: Load Historical Patterns

Read `_meta/analysis-patterns.md`, `_meta/analysis-phases.md`, and
`_meta/what-to-expect-algorithmic-interviews.md`. If stale (newer sessions exist
per CLAUDE.md), warn and recommend running `interview-repo-analyze` first.

## Step 2: Identify Target Repo

Two practice repos. Ask if not specified:

| Repo | Path | Use for |
|---|---|---|
| SentryEval | `/Users/eric/projects/SentryEval` | Python, algorithmic, OOP |
| learn-react | `/Users/eric/projects/learn-react` | Node, TypeScript, React, SQL |
| System design | — | Disconnected — do not evaluate |

Read the target repo's `CLAUDE.md`, then the relevant SKILL.md files:
- SentryEval: `oop-problem-gen`, `applied-oop-problem-gen`, `algo-problem-gen`
- learn-react: `start-session`, `end-session`, `scenario-practice`

## Step 3: Evaluate on Five Dimensions

For each skill:

1. **Phase structure** — does it match Phase 1 (given addressing) → 2 (find it) → 3 (optimize)?
   Mismatches: Phase 1 requires search; Phase 3 ceiling too high (heaps) or too low.
2. **Interface convention** — applied OOP = skeleton upfront; open-ended = discovery; algorithmic = I/O spec.
3. **Validation tests** — does it catch what real candidates fail at (extensibility), not sophistication metrics?
4. **Domain coverage** — do example domains produce the right shape/complexity?
5. **Complexity ceiling** — calibrated to 60 min? Above ceiling: segment trees, distributed coordination.

## Step 4: Gap Report

For each gap: dimension, what history shows, what the skill does, impact, recommendation.

Overall recommendation — one of: well-calibrated | update skill | write complementary skill | deprecate.

## Step 5: Next Action

Offer to proceed immediately if recommendation is (2) or (3).
