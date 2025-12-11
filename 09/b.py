#! /usr/bin/env python3

import pathlib

with pathlib.Path("test.txt").open() as f:
    vertices = [tuple(map(int, line.split(","))) for line in f]
numvertices = len(vertices)

#
# Convert to compressed coordinates
#  i.e. using indices of the sorted finite set of coordinates instead of real coordinates
X = sorted({x for x, y in vertices})
Y = sorted({y for x, y in vertices})
width = len(X)
height = len(Y)
copyvertices = [[X.index(x), Y.index(y)] for x, y in vertices]
vertices = [[X.index(x), Y.index(y)] for x, y in vertices]


#
# Define the region delimited by the path of connected red tiles
# as an array of width x height (in compressed coordinates) boolean values
def region(width, height, vertices):
    # Tell if the path of vertices delimiting the region turns
    #  clockwise (returns -4) or anti-clockwise (returns +4)
    def orientation():
        def by3(items):
            iterator = iter((*items, *items[:2]))
            a, b = next(iterator), next(iterator)
            for c in iterator:
                yield a, b, c
                a, b = b, c

        return sum(
            # compute the sign of the z coord of cross product
            # V1V2 X V2V3 where V1 V2 V3 are three consecutive vertices
            # the sum of which gives +/-4
            +1 if (x2 - x1) * (y3 - y2) > (y2 - y1) * (x3 - x2) else -1
            for (x1, x2, x3), (y1, y2, y3) in zip(by3(X), by3(Y), strict=True)
        )

    # The region is expanded by 0.5 units (of compressed coord)
    #  so that the vertical and horizontal lines have zero thickness.
    # The +/-0.5 shift on coordinates depends on the direction of each line and of the orientation
    if orientation() > 0:
        up    = +0.5
        down  = -0.5
        right = -0.5
        left  = +0.5
    else:
        up    = -0.5
        down  = +0.5
        right = +0.5
        left  = -0.5
    for i in range(len(vertices)):
        v1 = vertices[i-1]
        v2 = vertices[i]
        if v1[0] == v2[0]:
            # vertical line
            if v1[1] < v2[1]:
                v1[0] += up
                v2[0] += up
            else:
                v1[0] += down
                v2[0] += down
        elif v1[1] == v2[1]:
            # horizontal line
            if v1[0] < v2[0]:
                v1[1] += right
                v2[1] += right
            else:
                v1[1] += left
                v2[1] += left

    # we work on vertical lines, the only one used by the ray-tracing algorithm below
    verticalborders = []
    for i in range(len(vertices)):
        x1, y1 = vertices[i-1]
        x2, y2 = vertices[i]
        if x1 == x2:
            verticalborders.append((x1, min(y1, y2), max(y1, y2)))

    def pointinside(x, y):
        inside = False
        for xborder, ybordermin, ybordermax in verticalborders:
            if x < xborder and ybordermin < y < ybordermax:
                inside = not inside
        return inside

    return [[pointinside(x, y) for x in range(width)] for y in range(height)]


#for line in region(len(X), len(Y), vertices):
    #print("".join("X" if inside else "." for inside in line))

region = region(width, height, vertices)
areamax = 0
for i in range(len(copyvertices)-1):
    for j in range(i+1, len(copyvertices)):
        x1, y1 = copyvertices[i]
        x2, y2 = copyvertices[j]
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        #if all(region[y][x] for x in range(xmin, xmax + 1) for y in range(ymin, ymax + 1)):
        if True:
            area = (X[xmax] - X[xmin] + 1) * (Y[xmax] - Y[xmin] + 1)
            areamax = max(area, areamax)
print(areamax)

