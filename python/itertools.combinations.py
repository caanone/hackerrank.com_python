from itertools import combinations

chars, comb = input().split(" ")

for i in range(1, int(comb) + 1):
    print(sep="\n", *list("".join(x) for x in combinations(sorted(chars.upper()), i)))
