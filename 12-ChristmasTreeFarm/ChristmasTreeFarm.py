#! /usr/bin/env python3

import pathlib

with pathlib.Path("input.txt").open() as f:
    for _ in range(31):
        next(f)
    result = 0
    for line in f:
        a, b = line.split(":")
        w,h = map(int, a.split("x"))
        counters = [int(c) for c in b.split()]

        if (w//3) * (h//3) >= sum(counters):
            result += 1
    print("Part One:", result)
