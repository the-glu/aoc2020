
data = """16
10
15
5
1
11
7
19
6
12
4"""

data = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

data = list(sorted(map(int, data.split("\n"))))

with open("input", 'r') as f:
    data = list(sorted(map(lambda x: int(x), list(f.readlines()))))

dev = max(data) + 3
print(dev)


data = [0] + data + [dev]

cpos = 0

n1 = 0
n3 = 0

ok = True

chain = []

while ok:

    ok = False

    chain.append(data[cpos])

    if data[cpos] + 1 == data[cpos + 1]:
        n1 += 1
        cpos += 1
        ok = True
    else:
        for x in range(cpos, cpos + 3):
            if x < len(data) and data[cpos] + 3 == data[x]:
                n3 += 1
                cpos = x
                ok = True

    if not ok:
        print("???")

    if cpos == len(data) - 1:
        print("Done", n1, n3, n1 * n3)
        ok = False

print(chain)


splited_chains = []

cchain = []

for cpos in range(len(data)):

    if cpos > 1 and data[cpos] - data[cpos - 1] == 3:
        splited_chains.append(cchain)
        cchain = []

    cchain.append(data[cpos])

splited_chains.append(cchain)

print(splited_chains)

cchoices = 1

trinumbers = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096, 181997601, 334745777, 615693474, 113243685]

for subchain in splited_chains:

    cchoices *= trinumbers[len(subchain)]




print(cchoices)




# def findnext(pos):
#
#     for x in data:
#         if pos + 1 <= x <= pos + 3:
#             ndiff = findnext(x)
#
#             if ndiff is not None:
#                 n1, n3 = ndiff
#                 if x - pos == 3:
#                     n3 += 1
#                 elif x - pos == 1:
#                     n1 += 1
#                 return n1, n3
#
#     if pos + 3 == dev:
#         return 0, 1
#
#
# print(findnext(0))
