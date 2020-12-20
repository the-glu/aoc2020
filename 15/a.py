ns = [0,13,1,8,6,15]

lastcall = {}
previouslastcall = {}

cpos = 1

lastn = -1

for n in ns:

    print(n)
    lastn = n
    lastcall[lastn] = cpos
    cpos += 1

while cpos <= 30000000:

    # print(lastn, lastcall, previouslastcall)

    if lastn not in previouslastcall:
        lastn = 0
    else:
        lastn = lastcall[lastn] - previouslastcall[lastn]

    if cpos % 100000 == 0:
        print(cpos / 30000000, lastn)

    if lastn in lastcall:
        previouslastcall[lastn] = lastcall[lastn]

    lastcall[lastn] = cpos

    cpos += 1
