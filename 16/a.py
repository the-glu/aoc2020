data = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

with open("input", 'r') as f:
    data = "".join(list(f.readlines()))


dat_a = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""


cd = False
rules = {}
own_t = []
tickets = []

for x in data.split("\n"):

    if not x:
        continue

    if not cd:
        if x == "your ticket:":
            cd = True
        else:
            r, rest = x.split(": ", 1)
            p1, p2 = rest.split(" or ")
            rules[r] = (p1.split("-"), p2.split("-"))
    else:
        if not own_t:
            own_t = list(map(int, x.split(",")))
        else:
            if x != "nearby tickets:":
                tickets.append(list(map(int, x.split(","))))

print(rules)
print(own_t)
print(tickets)


nooktt = 0

tickets_ok = []

for t in tickets:

    tok = True

    for p in t:
        ok = False

        for rule in rules.values():
            for mi, ma in rule:
                if p >= int(mi) and p <= int(ma):
                    ok = True

        if not ok:
            nooktt += p
            tok = False

    if tok:
        tickets_ok.append(t)

print(nooktt)

print(tickets_ok)

possible_pos = {}

for k in rules.keys():

    possible_pos[k] = []

    for pos in range(len(tickets_ok[0])):
        possible_pos[k].append(pos)

print(possible_pos)

for t in tickets_ok:

    for pos, p in enumerate(t):

        for key, rule in rules.items():
            ok = False
            for mi, ma in rule:
                if p >= int(mi) and p <= int(ma):
                    ok = True

            if not ok:
                if pos in possible_pos[key]:
                    possible_pos[key].remove(pos)

print(possible_pos)

removed_something = True

while removed_something:
    removed_something = False

    for k, v in possible_pos.items():

        if len(v) == 1:

            v = v[0]

            for k2, v2 in possible_pos.items():
                if k2 == k:
                    continue

                if v in v2:
                    possible_pos[k2].remove(v)
                    removed_something = True

print(possible_pos)

t = 1

for k, pos in possible_pos.items():
    pos = pos[0]

    if k.startswith("departure"):
        t *= own_t[pos]

print(t)
