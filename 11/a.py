import sys


data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

with open("input", 'r') as f:
    data = "".join(list(f.readlines()))

m = {}

for x, yyy in enumerate(data.split("\n")):
    for y, i in enumerate(yyy):
        m[(x, y)] = i


def do_round(ma):

    nm = {}

    for p, v in ma.items():
        x, y = p

        if v == ".":
            nm[p] = "."
        elif v == "L":

            nval = "#"

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue

                    dm = 0
                    while True:

                        dm += 1

                        if (x + dx * dm, y + dy * dm) not in ma:
                            break

                        if ma[(x + dx * dm, y + dy * dm)] == "L":
                            break

                        if ma[(x + dx * dm, y + dy * dm)] == "#":
                            nval = "L"

            nm[p] = nval
        elif v == "#":
            c = 0

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue

                    dm = 0
                    while True:

                        dm += 1

                        if (x + dx * dm, y + dy * dm) not in ma:
                            break

                        if ma[(x + dx * dm, y + dy * dm)] == "L":
                            break

                        if ma[(x + dx * dm, y + dy * dm)] == "#":
                            c += 1
                            break


            nm[p] = "#" if c < 5 else "L"

    return nm


def priiint(m):
    for x in range(0, 10):
        for y in range(0, 10):
            print(m[(x, y)], end='')
        print('')
    print('')

c = 0


priiint(m)

while True:

    c += 1

    n = do_round(m)

    priiint(n)

    # if c > 3:
    #     sys.exit()

    if n == m:
        print(c)
        print(len(list(filter(lambda x: x == "#", n.values()))))

        sys.exit()

    m = n
