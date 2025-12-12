#! /usr/bin/env python3
import pathlib

with pathlib.Path("input.txt").open() as f:
    vertices = [list(map(int, line.split(","))) for line in f]
numvertices = len(vertices)


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
        # Compute the sign of the z coord of cross product
        #     V1V2 X V2V3
        # where V1 V2 V3 are three consecutive vertices
        # The sum of which gives +/-4 (if region is closed)
        +1 if (x2 - x1) * (y3 - y2) > (y2 - y1) * (x3 - x2) else -1
        for (x1, y1), (x2, y2), (x3, y3) in by3(vertices)
    )


# Expand the region by 0.5 units
#  so that the vertical and horizontal edges have zero thickness.
# The +/-0.5 shift on coordinates depends on the direction of
#  each edge and of the orientation of the region
regionvertices = [v[:] for v in vertices]
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
for i in range(len(regionvertices)):
    v1 = regionvertices[i-1]
    v2 = regionvertices[i]
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

# Keep separate vertical and horizontal edges of region
#  while sorting coordinates
verticaledges = [
    [x1, min(y1, y2), max(y1,y2)]
    for (x1, y1), (x2, y2) in zip(regionvertices, (*regionvertices[1:], regionvertices[0]), strict=True)
    if x1 == x2
]
horizontaledges = [
    [y1, min(x1, x2), max(x1,x2)]
    for (x1, y1), (x2, y2) in zip(regionvertices, (*regionvertices[1:], regionvertices[0]), strict=True)
    if y1 == y2
]


# Tell if a rectangle delimited by two of the original vertices is totally included in the region
#  the result if False if any of the 4 rectangle edge cross a region edge
def included(xmin, xmax, ymin, ymax):
    for xedge, yminedge, ymaxedge in verticaledges:
        if xmin < xedge < xmax:
            if yminedge < ymin < ymaxedge:
                return False
            if yminedge < ymax < ymaxedge:
                return False
    for yedge, xminedge, xmaxedge in horizontaledges:
        if ymin < yedge < ymax:
            if xminedge < xmin < xmaxedge:
                return False
            if xminedge < xmax < xmaxedge:
                return False
    return True


maxarea1 = maxarea2 = 0
for i in range(len(vertices) - 1):
    for j in range(i, len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[j]
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        area = (xmax - xmin + 1) * (ymax - ymin + 1)
        maxarea1 = max(maxarea1, area)
        if included(xmin, xmax, ymin, ymax):
            maxarea2 = max(maxarea2, area)
print("Part One:", maxarea1)
print("Part Two:", maxarea2)
