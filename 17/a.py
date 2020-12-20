

data = """.#.
..#
###"""

data = """..#..##.
#.....##
##.#.#.#
..#...#.
.###....
######..
.###..#.
..#..##."""

cube = {}

for x, l in enumerate(data.split("\n")):
    for y, p in enumerate(l):
        cube[(x, y, 0, 0)] = p


def update_m(cube):

    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0

    min_w = 0
    max_w = 0

    for (x, y, z, w), v in cube.items():
        if v == ".":
            continue
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if z < min_z:
            min_z = z
        if w < min_w:
            min_w = w

        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z
        if w > max_w:
            max_w = w

    return min_x, min_y, min_z, min_w, max_x, max_y, max_z, max_w

def iterate(cube):

    ncube = {}

    min_x, min_y, min_z, min_w, max_x, max_y, max_z, max_w = update_m(cube)

    for x in range(min_x - 2, max_x + 3):
        for y in range(min_y - 2, max_y + 3):
            for z in range(min_z - 2, max_z + 3):
                for w in range(min_w - 2, max_w + 3):

                    count = 0

                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            for dz in [-1, 0, 1]:
                                for dw in [-1, 0, 1]:
                                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                                        continue
                                    if cube.get((x + dx, y + dy, z + dz, w + dw), ".") == "#":
                                        count += 1

                    if cube.get((x, y, z, w), ".") == "#":
                        if count in [2, 3]:
                            ncube[(x, y, z, w)] = "#"
                        else:
                            ncube[(x, y, z, w)] = "."
                    else:
                        if count in [3]:
                            ncube[(x, y, z, w)] = "#"
                        else:
                            ncube[(x, y, z, w)] = "."

    return ncube

for x in range(0, 6):

    print(cube)

    cube = iterate(cube)


print(len(list(filter(lambda x: x == "#", cube.values()))))
