# Analysis: Algorithmic Patterns Observed

## Source
Derived from analysis of all interview sessions in this repository (March 2026).
Updated 2026-03-26: added TabaPay HackerRank session.
Updated 2026-05-11: added Mosaic take-home backend API session.
Updated 2026-05-20: added Axle fundamentals screen.
Updated 2026-06-12: added M.AI CodeSignal progressive UI screen.
Updated 2026-09-18: added Blue Shield system design session and SWE Open Call streaming screen.

## UI / front-end screens

> Distinct format: test suite queries the DOM via CSS selectors; tests pass/fail against rendered output, not logic. Levels unlock sequentially. No algorithmic reasoning required.

| Session | Problem | Stack |
|---|---|---|
| `240903-FrontEnd-React` | Payment progress bar — single component, derived state | React, TypeScript |
| `260611 - M.AI-React.AI` | Kanban board — 4 progressive levels (render → form → async fetch → status update) | React, TypeScript |

---

## Problems classified as algorithmic (live or automated screen)

> Note: `260511-Mosaic-Python` is a take-home backend API problem, not an algorithmic session. It is listed separately below but contributes Pattern 9.

| Session | Problem | Language |
|---|---|---|
| `241104-Bank` | Command dispatch — account system | Any |
| `250105-Baton-python` | Grid puzzle — sliding blocks | Python |
| `250121-Trailer-Yard` | Datetime interval filtering | Python |
| `250612-Everlaw-Java` | Word frequency counter | Java |
| `260130-Sentry` (01) | Stack trace profiler | Python |
| `260130-Sentry` (02) | Parking garage OOP | Python |
| `260320-Typescript-Node-React-Database` (01) | EventEmitter with interval + abort | TypeScript/Node |
| `260320-Typescript-Node-React-Database` (02) | SQL INSERT with JOIN | SQL |
| `260326-Python-HackerRank-TabaPay` (01) | Transaction Ledger — stdin aggregation | Python |
| `260326-Python-HackerRank-TabaPay` (02) | Spell Check — multiset frequency check | Python |
| `260917-SWE-OpenCall` (01) | Streaming JSONL parser — chunk buffering + newline framing | Python |

---

## System design sessions

> Distinct format: verbal or written architecture discussion. The evaluator drills into
> specific mechanics (auth internals, data flow, scale) rather than grading code. Noted here
> for completeness; no algorithmic practice-repo action. See individual session solutions.

| Session | Problem | Focus |
|---|---|---|
| `250903-GrowTherapy-SystemDesign` | System design | Architecture |
| `251010-DoorDash-SystemDesign` | System design | Architecture |
| `251120-Supio-SystemDesign` | Take-home doc | LLM pipeline |
| `260729-Blue-Shield` (01) | E-commerce platform — JWT/RBAC, async order flow, 100k users | Architecture |
| `260729-Blue-Shield` (02) | Backend domain — microservice chatter, resumable 1 TB upload | Architecture |

---

## Fundamentals / fluency screens

> Distinct format: multiple small, self-contained exercises at Phase 1 complexity. No progressive requirements. Tests language fluency, not algorithm design.

| Session | Exercises | Language |
|---|---|---|
| `260520-Axle` | Divisible filter, dict merge with collision sum, dedup keep-first, dedup keep-last | Python |

---

## Pattern 1: Progressive requirements

Every human-interviewer algorithmic problem adds layers mid-interview. You ship a working v1, then requirements are extended. Expect this in every live session.

- Parking garage: basic park → size-aware → distance-optimized → entrance/exit
- Bank: CREATE/ADD → TRANSFER/REPORT
- Everlaw: local impl → DB selection → corner cases → capacity planning
- Trailer Yard: parse → filter → (implied) invoice calculation

**Exception:** Automated screens (HackerRank) do not have progressive requirements — each problem is self-contained and graded pass/fail.

**Practice implication:** Write code that is easy to extend. Avoid hardcoding assumptions that the next requirement will break.

---

## Pattern 2: When to reach for a dict

A dict is the right first structure when the problem contains a **lookup**: "given X, find Y quickly."

| Problem | Lookup needed | Dict used for |
|---|---|---|
| Bank | Given account name, find balance | `name → balance` |
| Parking garage | Given license plate, find spot | `plate → spot_id` |
| Word counter | Given word, find count | `word → count` |
| Stack profiler | Given function name at this level, find node | `name → Node` (within tree) |
| Transaction Ledger | Given date or month, find totals | `(month, day) → [G_total, P_total]` |

**Dict merge with collision handling:** When two dicts share a key, the operation on collision must be explicit — sum (Axle), keep one, or raise an error. The cleanest implementation builds a fresh result dict and uses `.get(key, 0)` rather than branching on key existence. The Axle interview solution mutated one of the input dicts as a side effect — a common mistake noted explicitly in the interview code's docstring.

**When NOT to reach for dict first:**
- Stack profiler: primary structure is a **tree** (dict is secondary, inside nodes)
- Block puzzle: primary structure is the **2D grid** (already given)
- Trailer Yard filter: primary operation is **interval overlap** (logic, not lookup)
- Parking garage: primary thinking is **OOP** (dict is a lookup mechanism, not the design)

**The real skill:** Ask "what lookups do I need?" If you find yourself scanning a list repeatedly to find something, that's the signal to introduce a dict.

---

## Pattern 3: The shape of the data

Ask "what is the shape of this data?" before choosing a structure.

| Shape | Natural structure | Examples |
|---|---|---|
| "Given X, find Y" | dict | word counter, bank accounts |
| Hierarchical / parent-child | tree | stack profiler |
| Spatial / positional | 2D grid (list of lists/strings) | block puzzle |
| Objects with behavior and relationships | classes | parking garage |
| Ordered sequence with time intervals | list of objects | trailer yard events |
| "Can this request be satisfied by the pool?" | Counter / frequency dict | spell check |

---

## Pattern 4: Greedy reasoning

A greedy algorithm makes the locally best decision at each step without looking ahead.

**When it's safe:** when making a locally good choice cannot make future choices worse.
- Block puzzle: removing a block only clears space, never traps another block → greedy is safe
- Parking garage (distance): picking closest spot doesn't affect other cars → greedy is safe

**Interviewers want to hear the justification**, not just the choice: *"Greedy is safe here because X is monotonically beneficial — it can only open options, never close them."*

**Alternatives when greedy is not safe:**
- Backtracking: try a choice, undo if it fails
- BFS: shortest path over a state space
- Dynamic programming: overlapping subproblems with cached results

---

## Pattern 5: String normalization as a hidden requirement

Problems involving text nearly always require normalization that isn't stated upfront.

- Word counter: `"Twitter."` and `"twitter"` must match → lowercase + strip punctuation
- Stack profiler: function names are exact strings — no normalization, but insertion order matters
- Spell Check: input has spaces after commas → strip whitespace from each token

Interviewers ask "what corner cases did you miss?" after the happy path works. Have an answer ready.

---

## Pattern 6: Interval overlap

Appears in datetime problems. A naive equality check (`date == target_date`) misses events that span across midnight.

```
Event [entrance, exit] overlaps day D if:
  entrance <= end_of_day(D)  AND  (exit is None OR exit >= start_of_day(D))
```

`null` exit time = "still present" = treat as positive infinity.

---

## Pattern 7: Real-world framing — but not all problems are systems problems

Every problem in this repo uses a real-world domain. That is not the same as saying
every problem is free of algorithmic thinking. There are two distinct sub-types:

**Algorithmically-core problems** — the challenge is a recognizable CS algorithm or
data structure. The domain is the wrapper, not the challenge.
- Stack trace profiler: tree construction from flat input (a trie variant)
- Block puzzle: greedy grid traversal
- Word counter: stream aggregation into a dict
- Transaction Ledger: stdin aggregation with sort-then-print
- Spell Check: multiset frequency check
- These are closer to LeetCode in structure — the domain helps with edge cases but
  doesn't change the fundamental algorithm required.

**Systems-core problems** — the challenge is OOP design, extensibility, and state
management. The algorithm is trivial; the design is not.
- Parking garage, bank account: applied OOP with progressive requirements
- Trailer yard: datetime interval logic embedded in a real system
- These are not LeetCode-style — the algorithm is O(n) at most; the real test is
  whether the design holds up under Phase 2.

**Practice implication:** Know which type you are facing before you start.
Algorithmically-core problems reward pattern recognition. Systems-core problems
reward design instincts and extensibility awareness. Sentry, for example, asked
both in the same session — the profiler (algorithmic) and the parking garage (systems).

---

---

## Take-home backend API sessions

| Session | Problem | Stack |
|---|---|---|
| `260511-Mosaic-Python` | Bookstore inventory REST API + concurrent award updates | Python, PostgreSQL |

---

## Pattern 8: Multiset / frequency-map reasoning

Appears when the problem is "can this request be satisfied given a pool of resources?"
The resources and the request both have quantities per item — not just presence/absence.

- Spell Check: available letters have counts; each word needs counts; word passes iff every
  required count ≤ available count.

**Natural tool:** `collections.Counter`. Counter subtraction (`word_count - available`)
drops zero/negative results — the difference is empty `{}` exactly when all requirements
are met. This eliminates the need for a manual loop over letters.

**Generalizes to:** inventory checks, anagram detection, resource allocation with limits.

**Edge cases:** a letter needed more times than available (e.g., two `a`s but one in pool)
— Counter subtraction catches this; a set-membership check does not.

---

## Pattern 9: Concurrent writes to denormalized state

Appears when two tables must stay in sync and multiple requests may arrive simultaneously.
The classic form: a counter in table A is the sum of a field across rows in table B.

- Mosaic bookstore: `authors.num_total_awards` = sum of `books.num_awards` per author.
  An increment endpoint must update both atomically.

**What goes wrong without care:** two requests read `num_awards = 5` simultaneously,
both compute `6`, both write `6` — one increment is lost. This is a **lost update**.

**Three strategies — candidates must know all three and when each applies:**

| Strategy | Mechanism | Use when |
|---|---|---|
| Atomic SQL | `UPDATE books SET num_awards = num_awards + 1` | You don't need to read the value before writing |
| Pessimistic lock | `SELECT ... FOR UPDATE` inside a transaction | You need the current value to make a decision before writing |
| Optimistic lock | `version` column; retry if `WHERE id=? AND version=?` matches 0 rows | Low contention; prefer retry over blocking |

**Correct answer for this problem:** atomic SQL for both rows inside one transaction.
No application-side read needed — the DB handles the increment atomically, and the
transaction ensures both updates succeed or both roll back.

**Why this is a common interview weak spot:** ORMs hide this by default. Candidates
who haven't explicitly thought about it will reach for application-level logic or
not mention concurrency at all. Interviewers treat this as a significant signal.

**Coaching requirement:** any practice problem derived from this pattern must force the
candidate to name all three strategies, pick one with justification, and explain
why the others don't fit. Reciting definitions is not enough — the reasoning is the signal.

---

## Pattern 11: Async fan-out with per-item secondary fetch (React)

Appears when a primary API returns a list of items, some of which reference IDs that
must be resolved via a second API. The resolution is optional — the item renders fine
without it, but is enriched if the lookup succeeds.

- M.AI L3: fetch tasks list → for each task with `assignedUser` ID, fetch user name from
  Users API → merge name into task → render. If Users API returns 404, omit the owner field.

**React pattern:**
```tsx
useEffect(() => {
  fetch(TASKS_API)
    .then(r => r.json())
    .then(async tasks => {
      const enriched = await Promise.all(
        tasks.map(async t => {
          if (!t.assignedUser) return t;
          const res = await fetch(`${USERS_API}/${t.assignedUser}`);
          if (!res.ok) return t;           // 404 → omit enrichment
          const user = await res.json();
          return { ...t, ownerName: user.name };
        })
      );
      setTasks(enriched);
    });
}, []);
```

**Key decisions:**
- `Promise.all` parallelizes secondary fetches without violating "fetch one at a time" — the
  instructions said not to batch, not to serialize.
- `res.ok` check on the secondary call covers 404 gracefully; no error thrown to the user.
- The primary item is always rendered; the secondary enrichment is additive.

**Test surface:** CSS class name presence/absence. `card__owner` span is expected only
when a user name was successfully resolved. The test checks the DOM, not React state.

**Generalizes to:** any pattern where a list has optional foreign-key enrichment
(e.g., resolve avatar URLs, display names, tags).

---

## Pattern 12: Controlled form + state lifting

Appears when a form creates items that must immediately appear in a sibling component.
The form and the list share the same underlying collection — the collection state must
live in their common ancestor.

- M.AI L2: `CreateTaskForm` pushes a new task; `TaskColumn` renders the list.
  State (`todoItems`) lives in `App`, passed down as props.

**Validation:** client-side only. If either required field is empty, `return` before
calling `onAddTask`. Do not clear fields on failed submission.

**ID generation:** `uuid` library (`uuidv4()`) — generate at submission time, not render time.

**Generalizes to:** any "add to list" UI — comment forms, todo apps, item creators.

---

## Pattern 10: List deduplication with order preservation

Appears when a list may contain duplicate values and the output must preserve relative order.
The challenge is not detecting duplicates (trivial with a set) but deciding **which occurrence to keep**.

- Keep first: forward pass, `seen` set, append on first encounter only.
- Keep last: equivalent to reversing the list, applying keep-first, reversing the result.
  Alternatively: iterate backward, accumulate into a list, then `reversed()` it.

**Natural tool:** a `seen = set()` tracks which values have been encountered. O(n) time, O(n) space.

**Key subtlety (keep last):** a candidate who only knows the forward-pass pattern must reason about
traversal direction when the problem asks for last occurrence. The reversal trick is the cleanest path.

**Example:** `[0, 1, 2, 0, 3, 0]`  
- Keep first → `[0, 1, 2, 3]`  
- Keep last → `[1, 2, 3, 0]`

**Generalizes to:** deduplication in any ordered collection where recency vs. first-occurrence
semantics must be specified (event logs, user activity streams, ordered records).

---

## Pattern 13: Streaming ingestion — frame arbitrary chunks into records

Appears when data arrives as a stream of **arbitrary text chunks whose boundaries have no
relationship to the record boundaries**. A single record may be split across many `feed()`
calls, and one `feed()` may carry several records. The class must maintain buffer state
across calls and expose completed records at any time, including mid-stream.

- SWE Open Call: `StreamingJsonlParser` with `feed(chunk)` / `get_records()`. Input is
  JSONL (JSON values separated by newlines).

**The trap:** the record *looks* structural (`{ ... }`), so the tempting solution matches
braces. Brace matching fails on bare scalars (`true`, `42`), braces inside strings
(`"he said }"`), and nested objects (the first `}` is not the record's).

**The right primitive: find the frame, not the structure.** The only reliable delimiter is
the one the protocol guarantees — here the newline (JSONL forbids literal newlines inside a
value). The algorithm:

1. Append each chunk to a running buffer.
2. While a delimiter is present, cut the segment before it.
3. Validate the segment is a complete record — `json.loads` gives this for free; skip
   segments that don't parse (a malformed line is dropped, not fatal).
4. Keep the trailing unterminated remainder buffered for the next `feed`.
5. Return the accumulated records (as raw strings — not re-serialized objects).

**Distinct from stream aggregation (Pattern under "Stream aggregation"):** there, whole
events arrive as discrete items and you maintain a running total. Here the hard part is that
**record boundaries don't align with arrival boundaries**, so you must buffer partial input
and detect completeness.

**Hidden-test escalation:** this was an automated screen (CodeSignal-style, exact output,
16 hidden cases). The "phases" were smuggled into the test suite — plain objects, then
malformed lines, scalars, escaped braces in strings, deep nesting, and values split across
chunks. Enumerate these classes before submitting; there is no interviewer to reveal them.

**Generalizes to:** any framed transport — length-prefixed messages, newline/`\0`-delimited
protocols, log-line parsers, SSE/websocket consumers, incremental tokenizers.
