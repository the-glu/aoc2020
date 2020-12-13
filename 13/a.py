import sys
from collections import defaultdict

data = """939
7,13,x,x,59,x,31,19"""

data = """1000509
17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,739,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,971,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19"""


data = data.split("\n")


inits = int(data[0])

bus = []

for x in data[1].split(","):
    if x != "x":
        bus.append(int(x))
    else:
        bus.append(x)

print(inits, bus)

cpos = inits
done = False

while not done:
    for b in bus:
        if b == "x":
            continue
        if cpos % b == 0:
            print(b, cpos - inits, b * (cpos - inits))
            done = True
            break
    cpos += 1

####
for p, b in enumerate(bus):
    print(p, b)


pairs = []

for pos, b in enumerate(bus):

    if b == "x":
        continue

    for r in range(pos + b * -10, pos + b * 10, b):
        if r < 0:
            r += len(bus) + 1
        if r >= 0 and r < len(bus) and r != pos:
            if bus[r] != "x":
                pairs.append((b, bus[r]))

print(pairs)

paring = defaultdict(list)

def ppcm(*n):
    # https://python.jpvweb.com/python/mesrecettespython/doku.php?id=pgcd_ppcm
    def _pgcd(a, b):
        while b:
            a, b = b, a % b
        return a

    p = abs(n[0]*n[1]) // _pgcd(n[0], n[1])

    for x in n[2:]:
        p = abs(p*x) // _pgcd(p, x)

    return p

for p1, p2 in pairs:

    if p1 not in paring[p1]:
        paring[p1].append(p1)

    if p2 not in paring[p2]:
        paring[p2].append(p2)

    if p1 not in paring[p2]:
        paring[p2].append(p1)
    if p2 not in paring[p1]:
        paring[p1].append(p2)

bigest = 0
deltas = []

for nnn in paring.values():
    if ppcm(*nnn) > bigest:
        bigest = ppcm(*nnn)
        deltas = nnn


def testv(v):
    for pos, b in enumerate(bus):
        if b == "x":
            continue

        if (v + pos) % b != 0:
            return False

    return True

cpos = bigest
print(bigest)
print(deltas)

while True:

    for delta in deltas:
        if testv(cpos + delta):
            print(cpos + delta)
            sys.exit()
        if testv(cpos - delta):
            print(cpos - delta)
            sys.exit()

    cpos += bigest
