import math

data = """F10
N3
F7
R90
F11"""

with open("input", 'r') as f:
    data = "".join(list(f.readlines()))

data = data.split("\n")

pos = (0, 0)
ang = (1, 0)
way = (10, 1)

for l in data:
    if not l:
        continue
    a = l[0]
    u = int(l[1:])

    print(l, pos, end="")

    x, y = pos
    wx, wy = way

    if a == "N":
        way = (wx, wy + u)
    elif a == "S":
        way = (wx, wy - u)
    elif a == "E":
        way = (wx + u, wy)
    elif a == "W":
        way = (wx - u, wy)
    elif a == "F":
        pos = (x + way[0] * u, y + way[1] * u)
    elif a == "R":

        if u == 90 or u == 270:

            if ang == (1, 0):
                ang = (0, -1)
                way = (wy, -wx)
            elif ang == (0, -1):
                ang = (-1, 0)
                way = (wy, -wx)
            elif ang == (-1, 0):
                ang = (0, 1)
                way = (wy, -wx)
            elif ang == (0, 1):
                ang = (1, 0)
                way = (wy, -wx)

        if u >= 180:
            ang = (-ang[0], -ang[1])
            way = (-way[0], -way[1])

    elif a == "L":

        if u == 90 or u == 270:

            if ang == (1, 0):
                ang = (0, 1)
                way = (-wy, wx)
            elif ang == (0, -1):
                ang = (1, 0)
                way = (-wy, wx)
            elif ang == (-1, 0):
                ang = (0, -1)
                way = (-wy, wx)
            elif ang == (0, 1):
                ang = (-1, 0)
                way = (-wy, wx)

        if u >= 180:
            ang = (-ang[0], -ang[1])
            way = (-way[0], -way[1])


    print("->", pos)



print(pos)
print(abs(pos[0]) + abs(pos[1]))
