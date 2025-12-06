#! /usr/bin/env python3

import functools
import itertools
import pathlib

operators = {
    "+": int.__add__,
    "*": int.__mul__,
}


def problems_1():
    with pathlib.Path("input.txt").open() as f:
        # split the lines at blanks read the table by column (with the help of zip)
        # each column is a problem: a list of number ended by the operator (+ or *)
        # on the test example it gives:
        #  ('123', '45', '6', '*')
        #  ...
        for problem in itertools.zip_longest(*map(str.split, f.readlines()), fillvalue=" "):
            yield operators[problem[-1]], map(int, problem[:-1])


def problems_2():
    with pathlib.Path("input.txt").open() as f:
        operator = values = None
        # read the file by column of chars (with the help of zip)
        # each column is a number, the first one ends with the operator. each problem ends with an empty column
        # on the test example it gives:
        #  1  *
        #  24
        #  356
        #
        #  ...
        for column in map("".join, itertools.zip_longest(*f.readlines(), fillvalue=" ")):
            if not column.strip():
                yield operator, values
                continue
            if column[-1] in "+*":
                operator = operators[column[-1]]
                values = [int(column[:-1])]
            else:
                values.append(int(column))


print(
    "Part One:",
    sum(
        functools.reduce(operator, values) for operator, values in problems_1()
    ))
print(
    "Part Two:",
    sum(
        functools.reduce(operator, values) for operator, values in problems_2()
    ))
