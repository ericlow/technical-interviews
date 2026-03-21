import sys
import math
from contextlib import redirect_stdout


def solve(width, height, nb_blocks, grid):
    # Build a map of block_num -> list of (row, col) cells
    blocks = {}
    for r in range(height):
        for c in range(width):
            ch = grid[r][c]
            if ch.isdigit():
                n = int(ch)
                if n not in blocks:
                    blocks[n] = []
                blocks[n].append((r, c))

    for block_num, cells in blocks.items():
        for direction in ['UP', 'RIGHT', 'DOWN', 'LEFT']:
            if can_exit(grid, cells, direction, width, height):
                return f"{block_num} {direction}"

    return ''


def can_exit(grid, cells, direction, width, height):
    """
    A block can exit in a direction if every non-block cell that the block's
    trailing edge must sweep through is empty ('.').

    For non-contiguous blocks (C-shape, L-shape etc.), gaps within the block
    span must also be clear — the trailing cells will pass through them.

    LEFT:  for each row, check cols 0..max_col_in_row-1 (skip own cells)
    RIGHT: for each row, check cols min_col_in_row+1..width-1 (skip own cells)
    UP:    for each col, check rows 0..max_row_in_col-1 (skip own cells)
    DOWN:  for each col, check rows min_row_in_col+1..height-1 (skip own cells)
    """
    cell_set = set(cells)

    if direction == 'LEFT':
        rows = {}
        for r, c in cells:
            rows[r] = max(rows.get(r, 0), c)
        for r, max_c in rows.items():
            for c in range(0, max_c):
                if (r, c) not in cell_set and grid[r][c] != '.':
                    return False
        return True

    elif direction == 'RIGHT':
        rows = {}
        for r, c in cells:
            rows[r] = min(rows.get(r, width), c)
        for r, min_c in rows.items():
            for c in range(min_c + 1, width):
                if (r, c) not in cell_set and grid[r][c] != '.':
                    return False
        return True

    elif direction == 'UP':
        cols = {}
        for r, c in cells:
            cols[c] = max(cols.get(c, 0), r)
        for c, max_r in cols.items():
            for r in range(0, max_r):
                if (r, c) not in cell_set and grid[r][c] != '.':
                    return False
        return True

    elif direction == 'DOWN':
        cols = {}
        for r, c in cells:
            cols[c] = min(cols.get(c, height), r)
        for c, min_r in cols.items():
            for r in range(min_r + 1, height):
                if (r, c) not in cell_set and grid[r][c] != '.':
                    return False
        return True

    return False


# Ignore and do not change the code below
