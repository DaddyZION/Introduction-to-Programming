"""Assignment 3 – Exercise 3: Nested Loops"""

from __future__ import annotations

from typing import Iterable, List


def multiplication_table(size: int) -> List[List[int]]:
    table = []
    for row in range(1, size + 1):
        current = []
        for col in range(1, size + 1):
            current.append(row * col)
        table.append(current)
    return table


def render_table(table: Iterable[Iterable[int]]) -> None:
    print("=== MULTIPLICATION TABLE ===")
    for row in table:
        print(" ".join(f"{value:>4}" for value in row))


def checkerboard(rows: int, cols: int, symbols: str = "#.") -> List[str]:
    pattern = []
    for r in range(rows):
        line = []
        for c in range(cols):
            line.append(symbols[(r + c) % len(symbols)])
        pattern.append("".join(line))
    return pattern


def count_neighbors(grid: List[List[int]], r: int, c: int) -> int:
    total = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                total += grid[nr][nc]
    return total


def life_step(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    next_state = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(grid, r, c)
            if grid[r][c] == 1:
                next_state[r][c] = 1 if neighbors in (2, 3) else 0
            else:
                next_state[r][c] = 1 if neighbors == 3 else 0
    return next_state


def demo() -> None:
    table = multiplication_table(5)
    render_table(table)

    print("\n=== CHECKERBOARD ===")
    for row in checkerboard(6, 10):
        print(row)

    print("\n=== GAME OF LIFE STEP ===")
    start = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    result = life_step(start)
    for row in result:
        print(row)


if __name__ == "__main__":
    demo()
