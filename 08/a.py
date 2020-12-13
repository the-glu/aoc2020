import sys


data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

with open("input", 'r') as f:
    data = ''.join(f.readlines())

data = data.split("\n")[:-1]

for swapped_line in range(len(data)):

    a = 0
    p = 0

    exe = []

    while True:

        if p == len(data):
            print("Done", a)
            sys.exit(0)

        if p > len(data):
            break

        if p in exe:
            break

        exe.append(p)

        l = data[p]
        p += 1

        ins, val = l.split(" ")

        if p == swapped_line:
            if ins == "jmp":
                ins = "nop"
            elif ins == "nop":
                ins = "jmp"

        if ins == "acc":
            a += int(val)
        elif ins == "jmp":
            p += int(val) - 1
