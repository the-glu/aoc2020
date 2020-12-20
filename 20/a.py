from collections import defaultdict
import math

data = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""

with open("input", 'r') as f:
    data = "".join(list(f.readlines()))

tiles = {}


for b in data.split("\n\n"):

    if not b:
        continue

    l = b.split("\n")

    i = int(l[0][5:9])

    tiles[i] = list(map(list, l[1:]))


# print(tiles)

def pr(t):

    nn = len(t)

    for x in range(0, nn):
        for y in range(0, nn):
            print(t[x][y], end='')
        print('')

def rottt(t):
    ne = []
    nn = len(t)

    for x in range(0, nn):
        ne.append([])
        for y in range(0, nn):
            ne[x].append(t[nn - 1 - y][x])
    return ne


def hflip(t):

    ne = []
    nn = len(t)

    for x in range(0, nn):
        ne.append([])
        for y in range(0, nn):
            ne[x].append(t[nn - 1 - x][y])
    return ne


def vflip(t):
    ne = []
    nn = len(t)

    for x in range(0, nn):
        ne.append([])
        for y in range(0, nn):
            ne[x].append(t[x][nn - 1 - y])

    return ne

# pr(tiles[2311])
# print("--")
# pr(hflip(tiles[2311]))
# print("--")
# pr(vflip(tiles[2311]))
# print("--")
# pr(rot(tiles[2311]))
# print("--")
#
# print(rot(tiles[2311]) == tiles[2311])
# print(rot(rot(tiles[2311])) == tiles[2311])
# print(rot(rot(rot(tiles[2311]))) == tiles[2311])
# print(rot(rot(rot(rot(tiles[2311])))) == tiles[2311])

# All possible version

all_tiles_opts = {}

for tid, tiles in tiles.items():

    all_tiles_opts[tid] = []

    nbase = tiles

    for x in range(0, 4):

        nbase = rottt(nbase)

        if nbase not in all_tiles_opts[tid]:
            all_tiles_opts[tid].append(nbase)

        if hflip(nbase) not in all_tiles_opts[tid]:
            all_tiles_opts[tid].append(hflip(nbase))

        if vflip(nbase) not in all_tiles_opts[tid]:
            all_tiles_opts[tid].append(vflip(nbase))

        if hflip(vflip(nbase)) not in all_tiles_opts[tid]:
            all_tiles_opts[tid].append(hflip(vflip(nbase)))


    # print(len(all_tiles_opts[tid]))



# Compute all matching
bottom_matching = defaultdict(list)
right_matching = defaultdict(list)

for tid, atiles in all_tiles_opts.items():

    for otid, otiles in all_tiles_opts.items():
        if otid == tid:
            continue

        for ownr, owntiles in enumerate(atiles):
            for otherr, othertiles in enumerate(otiles):

                if owntiles[9] == othertiles[0]:
                    right_matching[tid].append((ownr, otid, otherr))

                bmatch = True

                for x in range(0, 9):
                    if owntiles[x][9] != othertiles[x][0]:
                        bmatch = False
                        break

                if bmatch:
                    bottom_matching[tid].append((ownr, otid, otherr))


print(bottom_matching)
print(right_matching)


llength = int(math.sqrt(len(all_tiles_opts.keys())))

print(llength)

# Compute possibles lines

def findright(cid, crot, chain, used):

    print(cid, crot, chain, used)

    if len(chain) == llength:
        return chain

    for ownr, otid, otherr in right_matching[cid]:

        if ownr != crot:
            continue

        if otid in used:
            continue

        newchain = chain[::]
        newchain.append((otid, otherr))

        newused = used[::]
        newused.append(otid)

        subchain = findright(otid, otherr, newchain, newused)

        if subchain:
            return subchain


possibles_lines = []

for tid, atiles in all_tiles_opts.items():

    for r, _ in enumerate(atiles):
        chain = findright(tid, r, [(tid, r)], [tid])
        if chain:
            possibles_lines.append(chain)


def findbottom(chain):

    if len(chain) == llength:
        return chain

    current_line = chain[-1]

    used_ids = list(map(lambda a: a[0], current_line))

    for oline in possibles_lines:

        lineok = True

        for pos, (oid, orot) in enumerate(oline):
            if oid in used_ids:
                lineok = False
                break

            cid, crot = current_line[pos]

            if (crot, oid, orot) not in bottom_matching[cid]:
                lineok = False
                break

        if lineok:
            nchain = chain[::]
            nchain.append(oline)

            subchain = findbottom(nchain)

            if subchain:
                return subchain

possible_orientations = []

for line in possibles_lines:

    chain = findbottom([line])

    if chain:
        possible_orientations.append(chain)

print(possible_orientations)

final_image = []

for ldata in possible_orientations[0]:

    for l in ldata:
        print(l[0], end=" ")
    print("")

    for x in range(1, 9):

        final_line = []

        for tid, rot in ldata:
            for y in range(1, 9):
                final_line += all_tiles_opts[tid][rot][y][x]

        # print(final_line)

        final_image.append(final_line)

for l in final_image:
    for y in l:
        print(y, end='')
    print("")


def find_fioupfioup(data):

    fioup = list(map(list, """                  #
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")))

    fioup[0].append(" ")  #....

    # for x in fioup:
    #     print(x)

    tt = 0

    for dx in range(0, len(data) - len(fioup[0])):
        for dy in range(0, len(data) - len(fioup)):

            found = True

            for x in range(0, len(fioup[0])):
                for y in range(0, len(fioup)):
                    if fioup[y][x] == "#" and data[y + dy][x + dx] == ".":
                        found = False

            if found:
                tt += 1

                for x in range(0, len(fioup[0])):
                    for y in range(0, len(fioup)):
                        if fioup[y][x] == "#":
                            data[y + dy][x + dx] = "O"

    dtt = 0
    for l in data:
        for x in l:
            if x == "#":
                dtt += 1

    # pr(data)

    return tt, dtt


nbase = final_image

for x in range(0, 4):

    nbase = rottt(nbase)

    print(find_fioupfioup(nbase))
    print(find_fioupfioup(hflip(nbase)))
    print(find_fioupfioup(vflip(nbase)))
    print(find_fioupfioup(hflip(vflip(nbase))))
