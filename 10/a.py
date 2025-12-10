#! /usr/bin/env python3

import functools
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
print("Part One:", xsum)




# def buttoniterator(joltages, lastpressed=0):
#     remainingcounters = {i for i in range(len(joltages)) if joltages[i]}
#     if remainingcounters & unreachablecounterswiththisbuttonandnextones[lastpressed]:
#         return
#     if forcedcounterswiththisbuttonandnextones[lastpressed] - remainingcounters:
#         return
#     for button in range(lastpressed, len(buttons)):
#         newjoltages = list(joltages)
#         for counter in buttons[button]:
#             newjoltages[counter] -= 1
#         if min(newjoltages) < 0:
#             continue
#         yield button, newjoltages




# def numpress(joltages, buttons):
#     joltages = list(joltages)
#     stack = [(joltages, buttoniterator(joltages))]
#     comb = []
#     while stack:
#         try:
#             button, joltages = next(stack[-1][1])
#             comb.append(button)
#             #print(comb, joltages)
#             if max(joltages) == 0:
#                 return len(comb)
#             stack.append((joltages, buttoniterator(joltages, button)))
#         except StopIteration:
#             comb.pop()
#             joltages, _ = stack.pop()
#     return len(stack)



# xsum = 0
# with pathlib.Path("test.txt").open() as f:
#     for i, line in enumerate(f):
#         items = line.split()
#         items.pop(0)
#         joltages = tuple(map(int, items[-1][1:-1].split(",")))
#         buttons = [set(map(int, b[1:-1].split(","))) for b in items[:-1]]
#         buttons.sort(key=len, reverse=True)
#         unreachablecounterswiththisbuttonandnextones = [
#             set(range(len(joltages))) - functools.reduce(set.union, buttons[button:]) for button in range(len(buttons))
#         ]
#         forcedcounterswiththisbuttonandnextones = [
#             functools.reduce(set.intersection, buttons[button:]) for button in range(len(buttons))
#         ]
#         print(i, joltages, buttons)
#         print(unreachablecounterswiththisbuttonandnextones)
#         print(forcedcounterswiththisbuttonandnextones)
#         # buttons = []
#         # for b in items[:-1]:
#         #     button = [0] * len(joltages)
#         #     for i in  map(int, b[1:-1].split(",")):
#         #         button[i] = 1
#         #     buttons.append(button)
#         num = numpress(joltages, buttons)
#         print(num)
#         print()
#         xsum += num
        
# print(xsum)


def buttoniterator(joltages, buttons, lastpressed=-1):
    if lastpressed != -1:
        remainingcounters = {i for i in range(len(joltages)) if joltages[i]}
        if remainingcounters & unreachablecounterswiththisbuttonandnextones[lastpressed]:
            return
        if forcedcounterswiththisbuttonandnextones[lastpressed] - remainingcounters:
            return
    for button in range(lastpressed+1, len(buttons)):
        maxcount = min(joltages[i] for i in range(len(joltages)) if i in buttons[button])
        for numpress in reversed(range(1, maxcount+1)):
            newjoltages = list(joltages)
            for counter in buttons[button]:
                newjoltages[counter] -= numpress
            yield button, numpress, newjoltages


def numpress(joltages, buttons):
    joltages = list(joltages)
    stack = [(joltages, buttoniterator(joltages, buttons))]
    combination = [(None, 0)]
    while stack:
        try:
            import sys
            print(combination, joltages, stack, file=sys.stderr)
            assert len(combination) == len(stack)
            button, numpress, joltages = next(stack[-1][1])
            print()
            combination.pop()
            combination.append((button, numpress))
            if max(joltages) == 0:
                return sum(numpress for button, numpress in combination)
            stack.append((joltages, buttoniterator(joltages, buttons, lastpressed=button)))
            combination.append((None, 0))
        except StopIteration:
            #print("stop!\n")
            combination.pop()
            joltages, _ = stack.pop()
    return 0



xsum = 0
with pathlib.Path("input.txt").open() as f:
    for i, line in enumerate(f):
        items = line.split()
        items.pop(0)
        joltages = tuple(map(int, items[-1][1:-1].split(",")))
        buttons = [set(map(int, b[1:-1].split(","))) for b in items[:-1]]
        buttons.sort(key=len, reverse=True)
        unreachablecounterswiththisbuttonandnextones = [
            set(range(len(joltages))) - functools.reduce(set.union, buttons[button:]) for button in range(len(buttons))
        ]
        forcedcounterswiththisbuttonandnextones = [
            functools.reduce(set.intersection, buttons[button:]) for button in range(len(buttons))
        ]
        print(i, joltages, buttons)
        print(unreachablecounterswiththisbuttonandnextones)
        print(forcedcounterswiththisbuttonandnextones)
        num = numpress(joltages, buttons)
        print(num)
        print()
        xsum += num
        break
        
print(xsum)
