#! /usr/bin/env python3

import functools
import itertools
import pathlib


def problems_1():
    "yields the problems (i.e. operator and numbers) according to first interpretation of worksheet"

    with pathlib.Path("input.txt").open() as f:
        # read the file by column (with the help of zip(*lines)) after splitting the lines on blanks
        #  each column is a problem: a list of numbers ended by the operator (+ or *)
        # On the test example it gives:
        #  ('123', '45', '6', '*')
        #  ...
        for problem in zip(*map(str.split, f), strict=True):
            yield problem[-1], map(int, problem[:-1])


def problems_2():
    "yields the problems (i.e. operator and numbers) according to second interpretation of worksheet"

    with pathlib.Path("input.txt").open() as f:
        operator = numbers = None
        # Read the file by column of chars (with the help of zip(*lines), actually
        #  zip_longuest(*lines) since not all lines are the same length)
        #  each column is a number, the first column of a problem ends with the operator
        # A blank column ends the problem
        # On the test example it gives:
        #  '1  *'
        #  '24  '
        #  '356 '
        #  '    '
        #  ...
        for column in map("".join, itertools.zip_longest(*f, fillvalue=" ")):
            if not column.strip():
                yield operator, numbers
                continue
            if column[-1] in "+*":
                operator = column[-1]
                numbers = [int(column[:-1])]
            else:
                numbers.append(int(column))


# Solving a problem is done with reduce() and the proper arithmetic operator
#  reduce(int.__mul__, (1, 24, 356)) → 8544
operators = {
    "+": int.__add__,
    "*": int.__mul__,
}
print(
    "Part One:",
    sum(
        functools.reduce(operators[op], numbers) for op, numbers in problems_1()
    ))
print(
    "Part Two:",
    sum(
        functools.reduce(operators[op], numbers) for op, numbers in problems_2()
    ))
