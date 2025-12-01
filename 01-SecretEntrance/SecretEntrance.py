#! /usr/bin/env python3

import pathlib

DIAL_COUNT = 100
START_POSITION = 50


def part1():
    dial = START_POSITION
    with pathlib.Path("input.txt").open() as f:
        for line in f:
            # lines look like: L68, L30 or R48
            rotation = int(line[1:])
            match line[0]:
                case "L":
                    dial = (dial - rotation) % DIAL_COUNT
                case "R":
                    dial = (dial + rotation) % DIAL_COUNT

            # +1 each time the arrow stops at 0
            if dial == 0:
                yield 1


def part2():
    dial = START_POSITION
    with pathlib.Path("input.txt").open() as f:
        for line in f:
            rotation = int(line[1:])

            # +1 each time the arrow makes a whole turn
            yield rotation // DIAL_COUNT
            rotation %= DIAL_COUNT

            if rotation == 0:
                continue
            match line[0]:
                case "L":
                    # +1 each time the arrow moves leftward over 0
                    if dial and dial - rotation <= 0:
                        yield 1
                    dial = (dial - rotation) % DIAL_COUNT
                case "R":
                    # +1 each time the arrow moves rightward over 0
                    if dial and dial + rotation >= DIAL_COUNT:
                        yield 1
                    dial = (dial + rotation) % DIAL_COUNT


print(f"Part #1: {sum(part1())}")
print(f"Part #2: {sum(part2())}")
