# Solution — Drill-Bank Account System

## Shape
Flat collection with name-based lookup → `dict[account_name → balance]`
Command routing → dispatch on operation string

## Phase analysis
- **Level 1** is a textbook Phase 1: given the operation and all arguments, just validate and mutate state. No searching, no optimization.
- **Level 2** introduces cross-account state (transfer requires reading two accounts simultaneously) and history (report requires storing past events, not just current state).

## Data structures
- `accounts: dict[str, int]` — account_name → current balance
- `history: dict[str, list]` — account_name → list of transactions (needed for REPORT)

## Solution

```python
def bank(operations):
    accounts = {}       # name -> balance
    history = {}        # name -> list of (timestamp, amount, type)
    results = []

    for op in operations:
        kind = op[0]

        if kind == "CREATE":
            _, ts, name = op
            if not name or name in accounts:
                results.append("")
            else:
                accounts[name] = 0
                history[name] = []
                results.append("true")

        elif kind == "ADD":
            _, ts, name, amount = op
            amount = int(amount)
            if name not in accounts:
                results.append("")
            else:
                accounts[name] += amount
                history[name].append((ts, amount, "ADD"))
                results.append(str(accounts[name]))

        elif kind == "TRANSFER":
            _, ts, src, dst, amount = op
            amount = int(amount)
            if (src not in accounts or
                dst not in accounts or
                src == dst or
                accounts[src] < amount):
                results.append("")
            else:
                accounts[src] -= amount
                accounts[dst] += amount
                history[src].append((ts, -amount, "TRANSFER_OUT"))
                history[dst].append((ts, amount, "TRANSFER_IN"))
                results.append(str(amount))

        elif kind == "REPORT":
            _, ts, name = op
            if name not in accounts:
                results.append("")
            else:
                results.append(str(history[name]))

    return results
```

## Key decisions

- **Dict for accounts**: `account_name → balance` — direct O(1) lookup for all operations
- **History list per account**: appended on every mutation; enables REPORT without reprocessing
- **All returns are strings**: convert integers with `str()`, booleans as literal `"true"`, failures as `""`
- **Transfer validation order**: check existence first, then same-account, then funds — fail fast

## Patterns
- Command dispatch (if/elif on operation type)
- Validate → mutate → record — consistent pattern across all operations
- Phase 1 characteristic: caller provides all addressing info (account names), no searching required
