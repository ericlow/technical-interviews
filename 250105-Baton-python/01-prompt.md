# Q1 — Sliding Block Puzzle (Python)

## Rules

A grid-based puzzle where wooden blocks must be removed one at a time without colliding.

- Each block is numbered 0 to nb_blocks-1
- A block slides in a direction until it either (a) exits the board or (b) collides
- Collision with another block or wall = **defeat**
- All blocks removed = **victory**
- If multiple blocks can move, you choose which
- If a block can exit multiple directions, you choose which
- Guaranteed: at least one valid solution exists

## Grid

- `.` = empty
- `x` = wall (immovable, can appear on borders)
- `0`–`nb_blocks-1` = block cells (same number = same block, always connected)

## Function signature

```python
def solve(width, height, nb_blocks, grid):
    # grid: list of `height` strings, each of length `width`
    # returns: string e.g. "1 RIGHT"
```

Called once per round. Parameters `width`, `height`, `nb_blocks` are constant. `grid` reflects current state.

## Output

`"<block_number> <DIRECTION>"` — direction is one of: `UP`, `RIGHT`, `DOWN`, `LEFT`

## Constraints

- 1 < width < 16
- 1 < height < 16
- 1 ≤ nb_blocks < 10

## Test cases (from platform)

- Few blocks, any order and any direction will work
- All blocks have a size of 1x1
- A space invader picture
- Only one possible solution
- Nested C-shaped blocks, no borders

## Open question

**Is every move required to exit the block?** Since collision = defeat, it seems like every chosen move must result in the block leaving the board. This has major algorithmic implications:

### Option A: Every move must exit a block (greedy is sufficient)

If blocks can only stop by exiting or colliding (and collision = defeat), then repositioning blocks within the board is impossible. In that case:
- At each step, find any block with a clear path to an edge (no walls or other blocks between it and the edge in that direction)
- Move it — it exits, reducing the problem by one block
- Repeat

A greedy "find any valid exit" works if removing a block never makes the remaining puzzle unsolvable. This is likely true since removing a block only clears space.

**Check for exit in direction LEFT:** for each row the block occupies, find its leftmost cell in that row; all cells between it and the left edge must be `.`
**RIGHT:** rightmost cell per row → right edge
**UP:** topmost cell per column → top edge
**DOWN:** bottommost cell per column → bottom edge

### Option B: Blocks can be repositioned (search required)

If a block can slide and stop against another block or wall without causing defeat (only moving INTO a wall/block during a forced slide causes defeat?), then the state space is larger and a BFS/DFS over game states may be needed to find the correct removal order.

This would be needed to pass the "only one possible solution" test if that test requires a specific ordering that greedy doesn't find.
