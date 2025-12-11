#! /usr/bin/env python3

import functools
import pathlib

with pathlib.Path("input.txt").open() as f:
    nodes = {name: children.split() for name, children in (l.split(":", maxsplit=1) for l in f)}
    nodes["out"] = []


#
# Recursive DFS with cache to count the path from node1 to node2
@functools.cache
def count(node1, node2):
    if node1 == node2:
        return 1
    children = nodes[node1]
    if not children:
        return 0
    return sum(count(child, node2) for child in children)


print("Part One:", count("you", "out"))
print("Part Two:",
    # We do not know if there are paths from 'fft' to 'dac' or from 'dac' to 'fft'
    # but it cannot go both ways. So lets compute both svr->fft->dac->out and svr->dac->fft->out
    # since at least one of the two is zero
    count("svr", "fft") * count("fft", "dac") * count("dac", "out") +
    count("svr", "dac") * count("dac", "fft") * count("fft", "out"),
)
