

data = """1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""


with open("input", 'r') as f:
    data = "".join(list(f.readlines()))

#
# def workon(ctt, op, tokens):
#
#     # print(tokens, ctt)
#     if not tokens:
#         return ctt, []
#
#     ct = tokens.pop(0)
#
#     clomode = False
#     nop = False
#
#     print(tokens, ct)
#
#     if ct[0] == "(":
#         ct, tokens = workon(0, "+", [ct[1:]] + tokens)
#     elif ")" in ct:
#
#         clomode = True
#
#         if ct[0] == ")":
#             nop = True
#         else:
#             basect = ct
#             ct = int(ct[:ct.index(")")])
#     elif ct in ["+", "*"]:
#         nop = True
#         tokens = [ct] + tokens
#     else:
#         ct = int(ct)
#
#     if not nop:
#         if op == "+":
#             ctt += ct
#         else:
#             ctt *= ct
#
#     if clomode:
#         nbclose = basect.count(")")
#         # print("POP")
#
#         if nbclose == "1":
#             return ctt, tokens
#         else:
#             return ctt, [")" * (nbclose - 1)] + tokens
#
#     if not tokens:
#         return ctt, []
#
#     oper = tokens[0]
#
#     ctt, tokens = workon(ctt, oper, tokens[1:])
#
#     return ctt, tokens


class MInt():

    def __init__(self, v):
        self.v = v

    def __add__(self, oint):
        return MInt(self.v * oint.v)

    def __sub__(self, oint):
        return MInt(self.v * oint.v)

    def __mul__(self, oint):
        return MInt(self.v + oint.v)

tt = 0

for l in data.split("\n"):

    if not l:
        continue

    def mapp(t):
        if t in ["(", " ", ")"]:
            return t
        if t == "*":
            return "-"
        if t == "+":
            return "*"
        return f"MInt({t})"

    newv = "".join(map(mapp, l))

    print(newv)

    r = eval(newv).v

    # r, __ = workon(0, "+", tokens)

    print(r)

    tt += r



print(tt)
