#! /usr/bin/env python3

import pathlib

boxes = []
with pathlib.Path("input.txt").open() as f:
    for line in f:
        x,y,z = line.split(",")
        boxes.append((int(x), int(y), int(z)))
print(len(boxes))


def distance(b1, b2):
    return (b2[0]-b1[0])**2 +(b2[1]-b1[1])**2 +(b2[2]-b1[2])**2


distances = []
for i in range(len(boxes)-1):
    b1 = boxes[i]
    for j in range(i+1, len(boxes)):
        b2 = boxes[j]
        distances.append((distance(b1,b2), i, j))

shortest = sorted(distances)[:1000]

# circuits = set()
# for _,i,j in shortest:
#     for c1 in circuits:
#         if i in c1:
#             circuits.discard(c1)
#             break
#     else:
#         c1 = None
#     for c2 in circuits:
#         if j in c2:
#             circuits.discard(c2)
#             break
#     else:
#         c2 = None
#     if c1 and c2:
#         circuits.add(c1 | c2)
#     elif c1:
#         circuits.add(c1 | {j})
#     elif c2:
#         circuits.add(c2 | {i})
#     else:
#         circuits.add(frozenset((i, j)))
# sizes = sorted(map(len, circuits), reverse=True)
# print(circuits)
# print(sizes)
# print(sizes[0]*sizes[1]*sizes[2])








connected = set()
circuits = set()
for _,i,j in sorted(distances):
    assert i != j
    for c1 in circuits:
        if i in c1:
            circuits.discard(c1)
            break
    else:
        c1 = None
    for c2 in circuits:
        if j in c2:
            circuits.discard(c2)
            break
    else:
        c2 = None
    if c1 and c2:
        assert c1 != c2
        circuits.add(c1 | c2)
    elif c1:
        circuits.add(c1 | {j})
    elif c2:
        circuits.add(c2 | {i})
    else:
        circuits.add(frozenset((i, j)))
    connected.add(i)
    connected.add(j)
    if len(connected) == 1000 and len(circuits) == 1:
        break
print(len(circuits))
print(len(circuits.pop()))
print(i,j)
print(boxes[i], boxes[j])
print(boxes[i][0] * boxes[j][0])
