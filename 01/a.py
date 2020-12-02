import itertools

with open("input", 'r') as f:
    numbers = list(map(lambda x: int(x), list(f.readlines())))

for a, b, c in itertools.combinations(numbers, 3):
    if a + b + c == 2020:
        print(a * b * c)
