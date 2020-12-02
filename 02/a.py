with open("input", 'r') as f:
    things = list(map(lambda x: x, list(f.readlines())))


o = 0

for x in things:
    v, l, t = x.split(" ")
    mi, ma = v.split("-")
    l = l[0]

    # if int(mi) <= t.count(l) <= int(ma):
    #     o += 1

    if l == t[int(mi)-1] or l == t[int(ma)-1]:
        if not (l == t[int(mi)-1] and l == t[int(ma)-1]):
            o += 1

print(o)
