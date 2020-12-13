

def p(s):

    r1, r2 = 0, 127
    c1, c2 = 0, 7

    for x in s:
        if x == 'F':
            r2 -= (r2 - r1 + 1) / 2
        elif x == 'B':
            r1 += (r2 - r1 + 1) / 2
        elif x == 'L':
            c2 -= (c2 - c1 + 1) / 2
        elif x == 'R':
            c1 += (c2 - c1 + 1) / 2
        # print(x, r1, r2, c1, c2)

    return r1, c1, r1 * 8 + c1

m = 0
ids = []

with open("input", 'r') as f:
    for l in f.readlines():
        _, _, i = p(l)
        if i > m:
            m = i
        ids.append(i)

print(m)

for x in range(int(m)):
    if x - 1 in ids and x + 1 in ids and x not in ids:
        print(x)

# print(p("BBFFBBFRLL"))

