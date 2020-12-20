import re

data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

with open("input", 'r') as f:
    data = "".join(list(f.readlines()))

dasta = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

# comask = 0
# camask = 0
# mem = {}
#
# for l in data.split("\n"):
#
#     if not l:
#         continue
#
#     if l.startswith("mask"):
#         mask = l.split(" = ")[1]
#
#         comask = int(mask.replace("X", "0"), 2)
#         camask = int(mask.replace("X", "1"), 2)
#
#     else:
#
#         pos, val = re.match(r"mem\[(\d*)\] = (\d*)", l).groups()
#
#         mem[int(pos)] = ((int(val) | comask) & camask)
#
# print(sum(mem.values()))


comask = 0
camask = 0
mem = {}
maskspos = []
basem = "000000000000000000000000000000000000"

for l in data.split("\n"):

    if not l:
        continue

    if l.startswith("mask"):
        mask = l.split(" = ")[1]

        comask = int(mask.replace("X", "0"), 2)
        camask = int(mask.replace("0", "1").replace("X", "0"), 2)

        maskspos = []

        for p, x in enumerate(mask):
            if x == "X":
                maskspos.append(p)

    else:

        pos, val = re.match(r"mem\[(\d*)\] = (\d*)", l).groups()

        baseaddr = (int(pos) | comask) & camask

        for v in range(0, 2 ** len(maskspos)):

            cm = list(basem)

            s = str(bin(v))[2:]

            while len(s) < len(maskspos):
                s = "0{}".format(s)

            for p, x in enumerate(s):
                if x == "1":
                    cm[maskspos[p]] = "1"

            mem[baseaddr | int(''.join(cm), 2)] = int(val)

print(sum(mem.values()))
