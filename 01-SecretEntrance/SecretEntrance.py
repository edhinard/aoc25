#! /usr/bin/env python3

import pathlib

DIAL_SIZE = 100
START_POSITION = 50


def rotations():
    with pathlib.Path("input.txt").open() as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])
            yield direction, distance


def pointatzero():
    position = START_POSITION
    count = 0
    for direction, distance in rotations():
        match direction:
            case "L":
                position = (position - distance) % DIAL_SIZE
            case "R":
                position = (position + distance) % DIAL_SIZE

        # count 1 each time the arrow stops at 0
        if position == 0:
            count += 1
    return count


def passoverzero():
    position = START_POSITION
    count = 0
    for direction, distance in rotations():

        # count 1 each time the arrow makes a whole turn
        count += distance // DIAL_SIZE
        distance %= DIAL_SIZE  # noqa: PLW2901
        if distance == 0:
            continue

        match direction:
            case "L":
                # count 1 each time the arrow moves leftward over 0
                if position and position - distance <= 0:
                    count += 1
                position = (position - distance) % DIAL_SIZE
            case "R":
                # count 1 each time the arrow moves rightward over 0
                if position and position + distance >= DIAL_SIZE:
                    count += 1
                position = (position + distance) % DIAL_SIZE
    return count


print("Part One:", pointatzero())
print("Part Two:", passoverzero())
