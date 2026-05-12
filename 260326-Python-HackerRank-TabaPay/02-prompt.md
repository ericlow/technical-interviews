---
title: Spell Check
source: TabaPay HackerRank screen
date: 2026-03-26
stack: Python
type: Algorithmic
---

## Problem Statement

Given a set of available letters and a list of words, return all words that can be
fully spelled using only the available letters. Each letter may be used only as many
times as it appears in the available set. Letter availability resets for each word
(words are checked independently).

## Input Format

```
Letters: <comma-separated single lowercase letters>
Words: <comma-separated lowercase words>
```

## Output Format

Comma-separated list of words that can be spelled, in the order they appeared in
the word list.

## Example Input

```
Letters: a, b, c, d, e, f
Words: bad, face, bead, xyz, cafe
```

## Example Output

```
bad, face, bead, cafe
```

> **Note:** The raw problem materials showed `bad, face, bead` as the example output
> but the accompanying explanation self-corrects: "actually cafe would pass." The
> correct output includes `cafe` — it needs c, a, f, e, all of which appear in the
> available set.
