#! /usr/bin/env python3

import dataclasses
import functools
import itertools
import pathlib

@dataclasses.dataclass
class Node:
    name: str
    nexts: list
    parents: list
    def __repr__(self):
        return f"{self.name}: {",".join(n.name for n in self.nexts)}"

nodes = [Node("out", [], [])]
with pathlib.Path("input.txt").open() as f:
    for line in f:
        name, nexts = line.split(":", maxsplit=1)
        node = Node(name, nexts.split(), [])
        nodes.append(node)
        if name == "you":
            you = node
        if name == "svr":
            svr = node
        if name == "dac":
            dac = node
        if name == "fft":
            fft = node
for node in nodes:
    node.nexts = [n for n in nodes if n.name in node.nexts]
    for next in node.nexts:
        next.parents.append(node)

#print(nodes)
#print(node)

#visited = {you}
queue = [(you, ("you",))]
count = 0
while queue:
    # for n,p in queue:
    #     print(n.name, "-".join(p))
    # print()
    current, path = queue.pop(0)
    for next in current.nexts:
        if next.name == "out":
            count += 1
            continue
        if next.name not in path:
            queue.append((next, (*path, next.name)))
print("part1",count)





queue = [(fft, ("fft",))]
fftsvr = 0
while queue:
    current, path = queue.pop(0)
    for parent in current.parents:
        if parent.name == "svr":
            fftsvr += 1
            continue
        queue.append((parent, (*path, parent.name)))
print("fft -> svr", fftsvr)

queue = [(fft, ("fft",))]
fftdac = 0
while queue:
    current, path = queue.pop(0)
    print(len(queue), len(path))
    for next in current.nexts:
        if next.name == "dac":
            fftdac += 1
            continue
        queue.append((next, (*path, next.name)))
print("fft -> dac", fftdac)


queue = [(dac, ("dac",))]
dacdown = 0
while queue:
    current, path = queue.pop(0)
    for next in current.nexts:
        if next.name == "out":
            dacdown += 1
            continue
        queue.append((next, (*path, next.name)))
print("dac -> out", dacdown)


print(fftsvr*dacdown*fftdac)



