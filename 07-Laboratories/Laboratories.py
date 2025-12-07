#! /usr/bin/env python3

import pathlib

with pathlib.Path("input.txt").open() as f:
    firstline = next(f).strip()

    # Part One
    #   simply count the splitters encountered by beams paths
    split = 0

    # Part Two
    #   pathcounts accumulate the number of paths for each columns
    #   after the first line pathcounts is filled with 0 except at the S column where there is 1 path
    pathcounts = [0] * len(firstline)
    pathcounts[firstline.index("S")] = 1

    for line in map(str.strip, f):
        for col, item in enumerate(line):
            if item == "^":
                count = pathcounts[col]

                # Part One
                #   +1 if a beam arrives at this splitter
                if count:
                    split += 1

                # Part Two
                #   after a splitter, the count at the splitter column becomes 0
                #   and the counts at left and at right are increased by the count of paths ending at the splitter
                pathcounts[col] = 0
                pathcounts[col-1] += count
                pathcounts[col+1] += count

print("Part One:", split)
print("Part Two:", sum(pathcounts))
