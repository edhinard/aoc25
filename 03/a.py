#! /usr/bin/env python3

import pathlib


count = 0
with pathlib.Path("input.txt").open() as f:
    for line in f:
        digits = [int(x) for x in line.strip()]
        posa = digits.index(max(digits[:-1]))
        b = max(digits[posa+1:])
        j = 10 * digits[posa] + b
        count += j
        #print(j)
print(count)


print()
count = 0
with pathlib.Path("input.txt").open() as f:
    for line in f:
        digits = [int(x) for x in line.strip()]
        j = 0
        pos = -1
        for i in reversed(range(12)):
            if i == 0:
                pos = digits.index(max(digits[pos+1:]), pos+1)
            else:
                pos = digits.index(max(digits[pos+1:-i]), pos+1)
            j = j*10 + digits[pos]
        count += j
        #print(j)
print(count)
