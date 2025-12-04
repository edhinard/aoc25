#! /usr/bin/env python3

import pathlib

# Prepare the two dimensions grid (row, column) with space all around
grid = []
with pathlib.Path("input.txt").open() as f:
    grid.extend(
        [".", *line.strip(), "."] for line in f
    )
grid.insert(0, ["."] * len(grid[0]))
grid.append(["."] * len(grid[0]))


MAXIMUM_ROLLS = 4


def ismovableroll(grid, row, col):
    # There is no roll in grid at this (row, col) position
    if grid[row][col] != "@":
        return False

    # Collect the 9 items around (row, col) in grid including the roll in the center
    around = (*grid[row-1][col-1:col+2], *grid[row][col-1:col+2], *grid[row+1][col-1:col+2])

    # The roll is movable if there are not too much other roll in the surrouding
    return around.count("@") < MAXIMUM_ROLLS + 1


count = None
while True:
    # List the movable rolls
    movablerollpositions = [
        (row, col) for row in range(len(grid)) for col in range(len(grid[0])) if ismovableroll(grid, row, col)
    ]

    if count is None:
        count = len(movablerollpositions)
        print("Part One:", count)
    else:
        count += len(movablerollpositions)

    # Effective removal of rolls or loop exit
    if len(movablerollpositions) == 0:
        break
    for row, col in movablerollpositions:
        grid[row][col] = "."

print("Part Two:", count)
