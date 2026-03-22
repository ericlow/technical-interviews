# Analysis: Algorithmic Patterns Observed

## Source
Derived from analysis of all interview sessions in this repository (March 2026).

## Problems classified as algorithmic

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

---

## Pattern 1: Progressive requirements

Every algorithmic problem adds layers mid-interview. You ship a working v1, then requirements are extended. Expect this in every session.

- Parking garage: basic park → size-aware → distance-optimized → entrance/exit
- Bank: CREATE/ADD → TRANSFER/REPORT
- Everlaw: local impl → DB selection → corner cases → capacity planning
- Trailer Yard: parse → filter → (implied) invoice calculation

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
