#! /usr/bin/env python3

import pathlib


def valid(ID):
    l = len(ID)
    if l % 2:
        return True
    return ID[:l//2] != ID[l//2:]


def part1():
    with pathlib.Path("input.txt").open() as f:
        idranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in f.read().split(",")]
    for a, b in idranges:
        for ID in range(a, b+1):
            if not valid(str(ID)):
                yield ID


def valid2(ID):
    for h in range(1, len(ID)):
        if len(ID) % h:
            continue
        if ID == ID[:h] * (len(ID) // h):
            return False
    return True

def part2():
    with pathlib.Path("input.txt").open() as f:
        idranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in f.read().split(",")]
    for a, b in idranges:
        for ID in range(a, b+1):
            if not valid2(str(ID)):
                yield ID


print(f"Part #1: {sum(part1())}")
print(f"Part #2: {sum(part2())}")
