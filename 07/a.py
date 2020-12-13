from collections import defaultdict
data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

data = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

with open("input", 'r') as f:
    data = ''.join(f.readlines())


mapping = {}
rmapping = defaultdict(list)

for x in data.split("\n"):
    if x:

        words = x.split(" ")

        fr = ' '.join(words[:2])

        mapping[fr] = []

        pos = 4

        while True:
            if pos > len(words) - 1:
                break

            if words[pos] == "no":
                break


            to = ' '.join(words[pos+1:pos+3])

            mapping[fr].append((to, int(words[pos])))

            rmapping[to].append((fr, int(words[pos])))

            pos += 4


d = ["shiny gold"]
td = [("shiny gold", 1)]

# p1
# while td:
#     tdd = td.pop(0)
#     for x, __ in rmapping[tdd]:
#         if x not in d:
#             d.append(x)
#             td.append(x)
#
# print(d)
# print(len(d) - 1)

tt = 0

while td:
    tdd, tc = td.pop(0)
    tt += tc
    for x, c in mapping[tdd]:
        td.append((x, c * tc))
    print(td)

print(tt - 1)
