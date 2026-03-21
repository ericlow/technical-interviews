# Drill-Bank — Account System (Progressive)

## Type
Algorithmic coding — command dispatch, OOP, progressive requirements

## Problem

Build a bank account system that processes a list of commands. Each command is a list:
`[OPERATION, timestamp, ...args]`

Return the result of each command as a list of strings. Return `""` for invalid operations.

## Level 1 — Account Creation + Deposits (10-15 min, ~15-20 lines)

### CREATE
`[CREATE, timestamp, account_name]`
- Creates a new account with the given name
- Returns `"true"` on success
- Returns `""` if name is empty or already exists

```
[CREATE, 1, account1] -> "true"
[CREATE, 2, account2] -> "true"

[CREATE, 1, account1] -> "true"
[CREATE, 2, account1] -> ""       # duplicate name

[CREATE, 1, ''] -> ""             # empty name
```

### ADD
`[ADD, timestamp, account_name, amount]`
- Adds amount to the account's balance
- Returns new balance as string
- Returns `""` if account does not exist

```
[CREATE, 1, account1] -> "true"
[CREATE, 2, account2] -> "true"
[ADD, 3, account2, 400] -> "400"
[ADD, 4, account1, 500] -> "500"
[ADD, 5, account1, 500] -> "1000"

[CREATE, 1, account1] -> "true"
[ADD, 2, account2, 400] -> ""     # account doesn't exist
```

## Level 2 — Transfers + Reporting (20-30 min, ~30-45 lines)

### TRANSFER
`[TRANSFER, timestamp, source_account, target_account, amount]`
- Transfers amount from source to target
- Returns transferred amount as string
- Returns `""` if: either account doesn't exist, source == target, or insufficient funds

```
[CREATE, 1, account1] -> "true"
[CREATE, 2, account2] -> "true"
[ADD, 3, account2, 100] -> "100"
[ADD, 4, account1, 200] -> "200"
[TRANSFER, 5, account1, account2, 50] -> "50"

[CREATE, 1, account1] -> "true"
[ADD, 2, account1, 200] -> "200"
[TRANSFER, 3, account1, account1, 50] -> ""   # same account
```

### REPORT
`[REPORT, timestamp, account_name]`
- Returns transaction history for the account (details TBD — not fully specified in source material)

## Notes
- Timestamps are integers, monotonically increasing
- All amounts are positive integers
- Return values are always strings (numbers as strings, booleans as `"true"`, failures as `""`)
