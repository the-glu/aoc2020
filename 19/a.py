data = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

with open("input", 'r') as f:
    data = "".join(list(f.readlines()))

datas = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
11: 42 31
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""


data = data.replace("8: 42", "8: 42 | 42 8")
data = data.replace("11: 42 31", "11: 42 31 | 42 11 31")


rules = {}
txts = []
rules_expended = []

d = False

for x in data.split("\n"):

    if not d:

        if not x:
            d = True
        else:

            pos, rst = x.split(": ")

            if rst[0] == '"':
                rules[int(pos)] = rst[1]
                rules_expended.append(int(pos))
            else:
                if "|" in rst:
                    p1, p2 = rst.split(" | ")
                else:
                    p1, p2 = rst, ""

                r1, r2 = [], []

                for y in p1.split(" "):
                    if y:
                        r1.append(int(y))

                for y in p2.split(" "):
                    if y:
                        r2.append(int(y))

                if r2:
                    rules[int(pos)] = [r1, r2]
                else:
                    rules[int(pos)] = [r1]


    else:

        if not d:
            continue

        txts.append(x)


print(rules)
print(txts)

max_length = max(map(len, txts))

expended = True

all_txt = "\n".join(txts)

while expended:

    expended = False

    ndict = {}
    nrules_expended = rules_expended[::]

    for rid, rul in rules.items():

        if rid in rules_expended:
            ndict[rid] = rul
        else:
            expendable = True
            for subr in rul:
                for i in subr:
                    if i != rid and i not in rules_expended:
                        expendable = False

            if expendable:
                expended = True
                nrules = []

                if rid == 8:

                    continue

                    # 8: 42 | 42 8

                    for ssrul in rules[42]:
                        nrules.append(ssrul)


                    done = False

                    while not done:

                        done = True

                        nnrules = []
                        print(".")
                        print(nrules)

                        for ssrul1 in rules[42]:
                            for ssrul2 in nrules:
                                ntxt = ssrul1 + ssrul2
                                if len(ntxt) < max_length:
                                    if ntxt in all_txt:
                                        if ntxt not in nrules:
                                            onem = True
                                            for txt in txts:
                                                if txt.startswith(ntxt):
                                                    onem = True
                                                    break

                                            if onem:
                                                done = False
                                                nnrules.append(ntxt)

                        nrules = nrules + nnrules

                elif rid == 11:

                    continue

                    # 11: 42 31 | 42 11 31

                    for ssrul1 in rules[42]:
                        for ssrul2 in rules[31]:
                            if ssrul1 + ssrul2 in all_txt:
                                nrules.append(ssrul1 + ssrul2)

                    done = False

                    while not done:

                        print(".")

                        done = True

                        nnrules = []

                        for ssrul1 in rules[42]:
                            for ssrul2 in nrules:
                                for ssrul3 in rules[31]:

                                    ntxt = ssrul1 + ssrul2 + ssrul3

                                    if len(ntxt) < max_length:
                                        if ntxt in all_txt:
                                            if ntxt not in nrules:

                                                onem = True
                                                for txt in txts:
                                                    if txt.endswith(ntxt):
                                                        onem = True
                                                        break

                                                if onem:
                                                    done = False
                                                    nnrules.append(ntxt)

                        nrules = nrules + nnrules

                else:
                    for subr in rul:

                        if len(subr) == 1:
                            for ssrul in rules[subr[0]]:
                                nrules.append(ssrul)
                        elif len(subr) == 2:

                            print(rid, rul)

                            for ssrul1 in rules[subr[0]]:
                                for ssrul2 in rules[subr[1]]:
                                    if ssrul1 + ssrul2 in all_txt:
                                        nrules.append(ssrul1 + ssrul2)

                        elif len(subr) == 3:

                            for ssrul1 in rules[subr[0]]:
                                for ssrul2 in rules[subr[1]]:
                                    for ssrul3 in rules[subr[2]]:
                                        if ssrul1 + ssrul2 + ssrul3 in all_txt:
                                            nrules.append(ssrul1 + ssrul2 + ssrul3)

                ndict[rid] = nrules
                nrules_expended.append(rid)
                # print(rid, rul, ndict[rid])
            else:
                ndict[rid] = rul


    rules = ndict
    rules_expended = nrules_expended

# print(rules)

print("C")

tt = 0

for txt in txts:
    if txt in rules[0]:
        tt += 1

print(tt)

tt = 0

for txt in txts:
    if not txt:
        continue

    btxt = txt

    ok = False

    # 42 * x  31 * y

    for x in rules[42]:
        if y in rules[31]:
            print(":(")


    nb42 = 0

    while txt:

        r = False

        for l in rules[42]:
            if txt.startswith(l):
                txt = txt[len(l):]
                r = True
                nb42 += 1
                # print(txt, "42")
                break

        if not r:
            break

    if not txt:
        print(btxt, "Not Matched (No 31)")
        continue

    while txt:

        r = False

        for l in rules[31]:
            if txt.startswith(l) and nb42 > 1:
                txt = txt[len(l):]
                r = True
                nb42 -= 1
                # print(txt, "31")
                break

        if not r:
            break

    if not txt:
        tt += 1
        print(btxt, "Matched")
    else:
        print(btxt, "Not Matched")


    # print(rules[42])
    # print(rules[31])

print(tt)
