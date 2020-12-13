import itertools
import sys

data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

data = list(map(int, data.split("\n")))

with open("input", 'r') as f:
    data = list(map(lambda x: int(x), list(f.readlines())))

print(data)

max_length = 25

buff = data[:max_length]

print(buff)

pos = max_length

for x in data[max_length:]:

    ok = False

    for a, b in itertools.combinations(buff, 2):
        if a + b == x:
            ok = True

    if not ok:
        print(x)
        break


    buff.append(x)
    buff.pop(0)

    pos += 1

for p1 in range(pos):

    csum = data[p1]
    r = [data[p1]]

    for p2 in range(p1 + 1, pos):
        r.append(data[p2])
        csum = sum(r)

        if csum == x:
            print(min(r) + max(r))
            sys.exit(0)

        if csum > x:
            break
