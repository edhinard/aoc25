#! /usr/bin/env python3

import pathlib


def listids():
    with pathlib.Path("input.txt").open() as f:
        for idrange in f.read().split(","):
            start, stop = map(int, idrange.split("-"))
            yield from range(start, stop+1)


def isnotvalid1(ID):
    ID = str(ID)
    numdigits = len(ID)
    return numdigits % 2 == 0 and ID[:numdigits//2] == ID[numdigits//2:]


def isnotvalid2(ID):
    ID = str(ID)
    numdigits = len(ID)
    for sequencelen in range(1, numdigits // 2 + 1):
        if numdigits % sequencelen:
            continue
        if ID[:sequencelen] * (numdigits // sequencelen) == ID:
            return True
    return False


print(f"Part One: {sum(ID for ID in listids() if isnotvalid1(ID))}")
print(f"Part Two: {sum(ID for ID in listids() if isnotvalid2(ID))}")
