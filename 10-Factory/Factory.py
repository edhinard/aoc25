#! /usr/bin/env python3

import itertools
import pathlib

import scipy


def numpressforlights(lights, buttons):
    # Testing all combinations of num buttons (order does not matter)
    #  from num=1 to num=<number of buttons
    # The first combination that gives the expected lights pattern wins
    for num in range(1, len(buttons)+1):
        for combination in itertools.combinations(buttons, num):
            currentlights = set()
            for button in combination:
                currentlights ^= button
            if currentlights  == lights:
                return num

    # No solution to problem
    return 0


def numpressforjoltages(joltages, buttons):
    # Finding integer numbers xi (the number of time button i should be pressed)
    # so that:
    #   - sum(xi) is minimum
    #   - linear combinations of xi equals the joltages vector (A.X = J)
    # This is a Linear Programming problem. Let's use a solver for that
    res = scipy.optimize.linprog(
        c=[1]*len(buttons),  # the function to minimize
        A_eq=[[int(j in button) for button in buttons] for j in range(len(joltages))],
        b_eq=joltages,

        method="highs", # only this method accept integrality parameter
        integrality=1,  # integer solution are required
    )
    if not res.success:
        # No solution to problem
        return 0

    # res.fun is the value of the minimum function, sometimes not exactly an integer
    return round(res.fun)


sum1 = sum2 = 0
with pathlib.Path("input.txt").open() as f:
    for line in f:
        items = line.split()
        lights = {i for i, light in enumerate(items.pop(0)[1:-1]) if light == "#"}
        joltages = tuple(map(int, items.pop()[1:-1].split(",")))
        buttons = [set(map(int, b[1:-1].split(","))) for b in items]

        sum1 += numpressforlights(lights, buttons)
        sum2 += numpressforjoltages(joltages, buttons)
print("Part One:", sum1)
print("Part Two:", sum2)
