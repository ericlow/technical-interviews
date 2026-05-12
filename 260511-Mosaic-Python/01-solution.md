# Solution: Bookstore Inventory Management System

## Approach

This is a standard CRUD API take-home with one non-trivial twist: concurrent updates to a denormalized counter (`num_total_awards`) that spans two tables. The schema is straightforward; the interesting design work is in the award-increment endpoint, where naive read-modify-write patterns produce lost updates under concurrency. The correct fix is a single atomic SQL statement or a row-level lock, not application-level logic.

---

## Phase Breakdown

### Phase 1 — Schema

- `books` and `authors` are a classic one-to-many: `books.author_id` FK → `authors.id`.
- `num_total_awards` on `authors` is a denormalized cache of `SUM(books.num_awards)`. This is intentional — it trades write complexity for read speed.
- `isbn` gets a `UNIQUE` constraint; `publication_time` is a `TIMESTAMP` or `DATE` depending on precision needed.

### Phase 2 — CRUD API

Standard REST endpoints. Key decisions:
- Return `404` for missing IDs consistently across GET, PUT, DELETE.
- `POST /books` should validate `isbn` uniqueness and return `409` on conflict.
- `author_id` is required on create; no author CRUD needed.

### Phase 3 — Concurrent Award Updates

**What goes wrong:** Two requests read `num_awards = 5` simultaneously, both compute `6`, both write `6` — one increment is lost. Same race applies to `num_total_awards` on the author row.

**Fix options:**

| Approach | How | Tradeoff |
|---|---|---|
| Atomic SQL | `UPDATE books SET num_awards = num_awards + 1 WHERE id = ?` | Simplest; correct for single-row updates |
| Pessimistic lock | `SELECT ... FOR UPDATE` then update in a transaction | Needed when you must read before writing (e.g., business logic on the value) |
| Optimistic lock | Add `version` column; retry on conflict | Better throughput under low contention; adds retry logic |

**Best answer here:** Use atomic SQL for both tables inside a single transaction:

```sql
BEGIN;
UPDATE books SET num_awards = num_awards + 1 WHERE id = ?;
UPDATE authors SET num_total_awards = num_total_awards + 1 WHERE id = (SELECT author_id FROM books WHERE id = ?);
COMMIT;
```

This eliminates the race without explicit locking. If two requests touch the same author via different books, the second `UPDATE` blocks until the first commits — correct behavior, minimal lock scope.

---

## Key Decisions

- **Denormalized `num_total_awards`** vs. computing it on read with `SUM()`: the problem specifies the column, so maintain it; note the tradeoff (writes are more complex, reads are O(1)).
- **Atomic increment vs. row lock**: atomic SQL is sufficient here; a `SELECT FOR UPDATE` is only necessary if you need the value before deciding whether to update.
- **Transaction scope**: both the book and author updates must be in the same transaction to avoid a window where `num_awards` is incremented but `num_total_awards` is not.

---

## Edge Cases

- Increment on a non-existent book ID — return `404`.
- Book with no author (orphaned row) — shouldn't happen if FK is enforced, but guard at the API layer.
- Soft-delete stretch: award increment on a soft-deleted book — should return `404` or `410`.
- Genre aliasing stretch: normalize genre on write so aliases are stored canonically, or store raw and normalize on read via a lookup table.

---

## Complexity

Not applicable (this is a system design / API take-home, not an algorithmic problem). Database operation costs are O(1) per row with indexed primary keys.

---

## What This Tests

Whether the candidate understands concurrency hazards in relational databases and can distinguish between naive read-modify-write, atomic SQL, and locking strategies — and can pick the right one for the constraint. Secondary signal: schema normalization judgment and clean REST API design.

---

## Coaching Note — Do Not Gloss Over Concurrency

This is one of the most commonly skipped topics in interview prep, and interviewers notice. Candidates who haven't thought about this before will either say nothing or reach for an application-level mutex, which is wrong in a multi-process web server context.

Any practice problem generated from this session **must** force the candidate to articulate the three strategies and when each applies:

- **Atomic SQL** — no read needed; let the database increment atomically. Correct here.
- **Pessimistic locking (`SELECT FOR UPDATE`)** — need to read the value before deciding what to write. Blocks concurrent transactions.
- **Optimistic locking (version column + retry)** — low contention expected; detect conflict at write time instead of preventing it.

The goal is not to recite definitions. The candidate should be able to look at a concrete scenario and say *which* strategy fits and *why* the others don't. That reasoning is what separates a passing answer from a strong one.
