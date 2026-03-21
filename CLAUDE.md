# Technical Interviews — Knowledge Base

## Purpose

A repository of real interview problems encountered across companies. Each problem is documented with a prompt (what was asked) and a solution (approach + code). The goal is to build a knowledge base for generating new practice problems.

## What's here

Each directory is one interview session, named `YYMMDD-Company-Stack`.

| Directory | Type | Stack |
|---|---|---|
| `240903-FrontEnd-React` | UI component (tech screen) | React, TypeScript |
| `240925-Resfrac-React-Node` | Full-stack take-home project | React, Electron, SQLite, OAuth2 |
| `241104-Bank` | Algorithmic — command dispatch, OOP | Language-agnostic |
| `250105-Baton-python` | Algorithmic — grid puzzle | Python |
| `250121-Trailer-Yard` | Algorithmic — datetime filtering | Python |
| `250612-Everlaw-Java` | Algorithmic + system design | Java |
| `250903-GrowTherapy-SystemDesign` | System design | Architecture |
| `251010-DoorDash-SystemDesign` | System design | Architecture |
| `251014-AWS-manager` | Backend API — concurrency, AWS SDK | Python or Go |
| `251120-Supio-SystemDesign` | System design (take-home doc) | Architecture, LLM pipeline |
| `260130-Sentry` | Algorithmic — OOP, tree traversal | Python |
| `260320-Typescript-Node-React-Database` | Algorithmic + SQL | TypeScript, Node.js, SQL |

## Naming convention

Every generated problem in a directory follows this scheme:

```
{NN}-prompt.md       # problem statement
{NN}-solution.md     # approach, reasoning, tradeoffs
{NN}-solution.{ext}  # runnable code (if applicable)
```

Where `NN` is a zero-padded integer (01, 02, ...) representing the problem number within that session. Some directories also contain original source files (PDFs, PNGs, .py, .txt) — these are raw materials, not generated content.

**Note:** `241104-Bank` and `251014-AWS-manager` contain a `problem.md` added by the user before the convention was established. The canonical files are `01-prompt.md` / `01-solution.md`.

## Analyses

Deeper analysis of patterns, difficulty, and data structures is in `_meta/`. Load these when generating new problems or studying patterns — do not load by default.

| File | Contents |
|---|---|
| `_meta/analysis-patterns.md` | Data structure and algorithmic patterns observed across all problems |
| `_meta/analysis-phases.md` | How interview problems escalate in difficulty (Phase 1–4 framework) |

## Instructions for future sessions

- To understand a specific interview: read `{directory}/01-prompt.md`
- To see the solution approach: read `{directory}/01-solution.md`
- To generate new practice problems: read `_meta/` files first, then load relevant prompts by domain
- Do not load all files at once — use the directory table above to select what is relevant
- Prefer editing existing `prompt.md` / `solution.md` files over creating new top-level files
