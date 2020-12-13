

data = """abc

a
b
c

ab
ac

a
a
a
a

b
"""

with open("input", 'r') as f:
    data = ''.join(f.readlines())

u = 0

ans = []
f = True

for x in data.split("\n"):
    if not x:
        print(ans)
        u += len(ans)
        ans = []
        f = True
    else:
        if f:
            for xx in x:
                if xx not in ans:
                    ans.append(xx)
            f = False
        else:
            for xx in list(ans[::-1]):
                if xx not in x:
                    ans.remove(xx)


print(u)
