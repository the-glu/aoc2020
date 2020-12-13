

with open("input", 'r') as f:
    data = ''.join(f.readlines())

dasta = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

data = data.split("\n")
data = data[:-1]
# print(data)

tt = 1

for dx, dy in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    posx = 0
    posy = 0

    # dx = 1
    # dy = 3

    ccount = 0

    while posx < len(data):

        print(data[posx])

        if data[posx][posy % len(data[posx])] == '#':
            ccount += 1

        posx += dx
        posy += dy

    print(ccount)
    tt = tt * ccount

print(tt)
