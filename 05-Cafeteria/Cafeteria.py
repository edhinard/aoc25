#! /usr/bin/env python3

import pathlib

with pathlib.Path("input.txt").open() as f:
    # Read ranges
    ranges = []
    for line in f:
        if not line.strip():
            break
        first, last = map(int, line.split("-"))
        ranges.append((first, last))

    # and IDs
    IDs = [int(line) for line in f]


count = 0
for i in IDs:
    for first, last in ranges:
        if i >= first and i <= last:
            count += 1
            break
print("Part One:", count)


freshranges = []
# Sort ranges by "first" in reverse order so that
#  we know "first" is not any already processed range
for first, last in sorted(ranges, reverse=True):

    # Merge [first;last] range with any [a;b] range it overlaps
    while freshranges:
        a,b = freshranges.pop(0)
        if last < a-1:
            freshranges.insert(0, (a,b))
            break
        last = max(last, b)  # noqa: PLW2901
    # and insert this range at the beginning of ranges
    # We know now that ranges are disjoint
    freshranges.insert(0, (first, last))

count = 0
for first, last in freshranges:
    count += last - first + 1
print("Part Two:",count)
