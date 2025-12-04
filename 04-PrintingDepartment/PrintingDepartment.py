#! /usr/bin/env python3

import pathlib


map = []
with pathlib.Path("input.txt").open() as f:
    for line in f:
        map.append((".", *line.strip(), "."))
map.insert(0, ["."] * len(map[0]))
map.append(["."] * len(map[0]))

count = 0
for col in range(len(map[0])):
    for row in range(len(map)):
        if map[row][col] == "@":
            t = 0
            for c in (-1,0,1):
                for r in (-1,0,1):
                    if map[row+r][col+c] == "@":
                        t += 1
            if t < 5:
                count += 1
print(count)





map = []
with pathlib.Path("input.txt").open() as f:
    for line in f:
        map.append([".", *line.strip(), "."])
map.insert(0, ["."] * len(map[0]))
map.append(["."] * len(map[0]))

count = 0
while True:
    toberemoved = []
    for col in range(len(map[0])):
        for row in range(len(map)):
            if map[row][col] == "@":
                t = 0
                for c in (-1,0,1):
                    for r in (-1,0,1):
                        if map[row+r][col+c] == "@":
                            t += 1
                if t < 5:
                    toberemoved.append((row,col))
    if len(toberemoved) == 0:
        break
    count += len(toberemoved)
    for row, col in toberemoved:
        map[row][col] = "."
print(count)