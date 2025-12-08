#! /usr/bin/env python3

import math
import pathlib

PART1_STOP_CRITERIA = 1000

# Read boxes coordinates
with pathlib.Path("input.txt").open() as f:
    boxes = [tuple(map(int, line.split(","))) for line in f]


# Loop on pair of boxes (b1, b2) from closest to farthest
distances = sorted(
    (math.dist(boxes[b1], boxes[b2]), b1, b2) for b1 in range(len(boxes) - 1) for b2 in range(b1 + 1, len(boxes))
)
circuits = set()
for i, (_, b1, b2) in enumerate(distances, start=1):
    # Find the circuits c1 and c2 containing boxes b1 and b2 respectively and remove then from circuits set
    for c1 in circuits:
        if b1 in c1:
            circuits.discard(c1)
            break
    else:
        c1 = None
    for c2 in circuits:
        if b2 in c2:
            circuits.discard(c2)
            break
    else:
        c2 = None

    # Add to the circuits set the new circuit resulting from the connection between b1 and b2
    if c1 and c2:
        circuits.add(c1 | c2)
    elif c1:
        circuits.add(c1 | {b2})
    elif c2:
        circuits.add(c2 | {b1})
    else:
        circuits.add(frozenset((b1, b2)))

    if i == PART1_STOP_CRITERIA:
        # "multiply together the sizes of the three largest circuits"
        circuitsizes = sorted(map(len, circuits), reverse=True)
        print("Part One:", circuitsizes[0] * circuitsizes[1] * circuitsizes[2])

    if i > 1 and len(circuits) == 1:
        "multiply together the X coordinates of the last two junction boxes you need to connect"
        print("Part Two:", boxes[b1][0] * boxes[b2][0])
        break
