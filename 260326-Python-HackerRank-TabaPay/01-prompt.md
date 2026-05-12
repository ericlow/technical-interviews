---
title: Transaction Ledger
source: TabaPay HackerRank screen
date: 2026-03-26
stack: Python
type: Algorithmic
---

## Problem Statement

Read a series of comma-separated lines from stdin. Each line has four fields:

| Field | Format | Values |
|---|---|---|
| month | zero-padded two-digit integer | `01`–`12` |
| day | zero-padded two-digit integer | `01`–`31` |
| type | single character | `G` (pay-in) or `P` (pay-out) |
| amount | float | positive |

Output two reports:

1. **By Date** — sorted by date (month then day). For each unique date, show total G and total P.
2. **By Month** — sorted by month. For each unique month, show total G and total P.

All amounts formatted to two decimal places. If no transactions of a type occur on a date, show `0.00`.

## Example Input

```
12,01, G, 0.25
12,01, P, 1.50
12,15, G, 3.00
10,04, P, 1.12
10,04, G, 0.50
```

## Example Output

```
By Date:
10/04: G=0.50, P=1.12
12/01: G=0.25, P=1.50
12/15: G=3.00, P=0.00

By Month:
10: G=0.50, P=1.12
12: G=3.25, P=1.50
```
