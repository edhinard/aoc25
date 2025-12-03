#! /usr/bin/env python3

import pathlib


def joltage(bank, length):
    ratings = list(map(int, bank))
    joltage = 0
    for i in reversed(range(length)):
        # locate first highest joltage rating, skipping last i -> pos
        pos = ratings.index(max(ratings)) if i == 0 else ratings.index(max(ratings[:-i]))

        # update total joltage with rating value at pos
        joltage = joltage * 10 + ratings[pos]

        # skip first rating values until pos
        ratings = ratings[pos+1:]
    return joltage


with pathlib.Path("input.txt").open() as f:
    print(
        "Part One:",
        sum(
            joltage(bank, 2) for bank in map(str.strip, f)
        ))
with pathlib.Path("input.txt").open() as f:
    print(
        "Part Two:",
        sum(
            joltage(bank, 12) for bank in map(str.strip, f)
        ))

