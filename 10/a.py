#! /usr/bin/env python3

import itertools
import pathlib


def numpress(lights, buttons):
    for num in range(1, len(buttons)+1):
        for combination in itertools.combinations(buttons, num):
            l = set()
            for b in combination:
                l = l ^ b
            if l  == lights:
                return num
    xxx
    return 0

xsum = 0
with pathlib.Path("input.txt").open() as f:
    for line in f:
        items = line.split()
        lights = {i for i,l in enumerate(items.pop(0)[1:-1]) if l == "#"}
        buttons = [set(map(int, b[1:-1].split(","))) for b in items[:-1]]
        num = numpress(lights, buttons)
        xsum += num
print(xsum)




def buttoniterator(joltages):
    imax = joltages.index(max(joltages))
    for b in buttons:
        newjoltages = list(joltages)
        if not b[imax]:
            continue
        for i in b:
            newjoltages[i] -= 1
        if min(newjoltages) < 0:
            continue
        yield newjoltages
    for b in buttons:
        newjoltages = list(joltages)
        if b[imax]:
            continue
        for i in b:
            newjoltages[i] -= 1
        if min(newjoltages) < 0:
            continue
        yield newjoltages




def numpress(joltages, buttons):
    joltages = list(joltages)
    combination = []
    while joltages:
        bit = buttoniterator(joltages)
        combination.append((joltages, bit))
        try:
            joltages = next(bit)
        except StopIteration:
            print(".")
            joltages, _ = combination.pop()
    return len(combination)



xsum = 0
with pathlib.Path("input.txt").open() as f:
    for line in f:
        items = line.split()
        items.pop(0)
        joltages = tuple(map(int, items[-1][1:-1].split(",")))
        buttons = [tuple(map(int, b[1:-1].split(","))) for b in items[:-1]]
        # buttons = []
        # for b in items[:-1]:
        #     button = [0] * len(joltages)
        #     for i in  map(int, b[1:-1].split(",")):
        #         button[i] = 1
        #     buttons.append(button)
        num = numpress(joltages, buttons)
        print(num, joltages, buttons)
        xsum += num
print(xsum)
