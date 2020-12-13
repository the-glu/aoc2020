import re


with open("input", 'r') as f:
    data = ''.join(f.readlines())

dasta = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

daata = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

daata = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

passports = []

cpassport = {}

for d in data.split("\n"):

    if not d:
        if cpassport.keys():
            passports.append(cpassport)
            cpassport = {}

    for sf in d.split(" "):
        if sf:
            k, v = sf.split(":")
            cpassport[k] = v

ok = 0

for p in passports:

    oo = True

    for f in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if f not in p:
            oo = False

    if not oo:
        continue

    try:
        byr = int(p["byr"])

        if byr < 1920 or byr > 2002:
            oo = False
    except Exception as e:
        oo = False

    if not oo:
        print("byr inva", p["byr"])
        continue
    print("byr ok", p["byr"])

    try:
        iyr = int(p["iyr"])

        if iyr < 2010 or iyr > 2020:
            oo = False
    except Exception as e:
        oo = False

    if not oo:
        print("iyr inva", p["iyr"])
        continue
    print("iyr ok", p["iyr"])

    try:
        eyr = int(p["eyr"])

        if eyr < 2020 or eyr > 2030:
            oo = False
    except Exception as e:
        oo = False

    if not oo:
        print("eyr inva", p["eyr"])
        continue
    print("eyr ok", p["eyr"])

    try:
        hgt, t = re.match(r"(\d*)(cm|in)", p["hgt"]).groups()
    except Exception as e:
        print(p["hgt"], "invalid (reg)")
        continue

    hgt = int(hgt)

    if t == "cm":
        if hgt < 150 or hgt > 193:
            oo = False
    else:
        if hgt < 59 or hgt > 76:
            oo = False

    if not oo:
        print("hgt inva", p["hgt"])
        continue
    print("hgt ok", p["hgt"])

    if not re.match("#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]", p["hcl"]):
        oo = False

    if not oo:
        print("hcl inva", p["hcl"])
        continue
    print("hcl ok", p["hcl"])

    if p["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        oo = False

    if not oo:
        print("ecl inva", p["ecl"])
        continue
    print("ecl ok", p["ecl"])

    if not re.match(r"^\d\d\d\d\d\d\d\d\d$", p["pid"]):
        oo = False

    if not oo:
        print("pid inva", p["pid"])
        continue
    print("pid ok", p["pid"])

    if oo:
        ok += 1


print(ok)
