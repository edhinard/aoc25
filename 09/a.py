#! /usr/bin/env python3

import math
import pathlib


with pathlib.Path("input.txt").open() as f:
    vertices = []
    for line in f:
        x, y = map(int, line.split(","))
        vertices.append((x, y))
numvertices = len(vertices)

# xs = [x for x,y in vertices]
# ys = [y for x,y in (*vertices[1:], vertices[0])]
# assert xs[::2] == xs[1::2]
# assert ys[::2] == ys[1::2]

area = []
for x1,y1 in vertices:
    for x2,y2 in vertices:
        area.append(abs((x2-x1+1) * (y2-y1+1)))
print(sorted(area)[-1])

# xmin = min(x for x,y in vertices)
# xmax = max(x for x,y in vertices)
# region = {}
# for x in range(xmin, xmax+1):
#     print(x,xmax+1)
#     crossings = []
#     for i in range(numvertices):
#         x1, y1 = vertices[i-1]
#         x2, y2 = vertices[i]
#         if y1 == y2:
#             # horizontal edge
#             if x1 < x2:
#                 # left to right
#                 if x1 <= x <= x2:
#                     crossings.append((y1, "LR"))
#             else:  # noqa: PLR5501
#                 # right to left
#                 if x2 <= x <= x1:
#                     crossings.append((y1, "RL"))
#     crossings.sort()
#     region[x] = []
#     previousdirection = None
#     while crossings:
#         miny, direction = crossings.pop(0)
#         assert previousdirection != direction
#         if crossings[0][1] == direction:
#             crossings.pop(0)
#         maxy, direction = crossings.pop(0)
#         if crossings and crossings[0][1] == direction:
#             maxy, previousdirection = crossings.pop(0)
#         region[x].append((miny, maxy))
# print(region)

# def included(i, j):
#     x1, y1 = vertices[i]
#     x2, y2 = vertices[j]
#     if x1 > x2:
#         x1, x2 = x2, x1
#     if y1 > y2:
#         y1, y2 = y2, y1
#     for x in range(x1, x2+1):
#         for miny, maxy in region[x]:
#             if y1 < miny or y2 > maxy:
#                 return False
#     return True

xcoords = sorted({x for x, y in vertices})
ycoords = sorted({y for x, y in vertices})
region = [[0] * len(ycoords)] * len(xcoords)

for x1, y1, x2, y2 in (compressedpair(i, i-1) for i in range(len(vertices)):
    pass

def compressedpair(i, j):
    x1, y1 = vertices[i]
    x2, y2 = vertices[j]
    xmin, xmax = min(x1, x2), max(x1, x2)
    ymin, ymax = min(y1, y2), max(y1, y2)
    return xcoords.index(xmin), ycoords.index(ymin), xcoords.index(xmax), ycoords.index(ymax)


area = []
for i in range(numvertices-1):
    for j in range(i+1, numvertices):
        # Rectangle defined by two of the vertices
        xmin, ymin, xmax, ymax = compressedpair(i, j)
        if overlap(xmin, ymin, xmax, ymax):
            area.append((xmax-xmin+1) * (ymax-ymin+1))
print(sorted(area)[-1])


# 9003540 too low
