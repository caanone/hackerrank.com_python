from itertools import permutations

if __name__ == "__main__":
    chars, comb = input().split(" ")

    print(sep="-", end="", *list("".join(x) for x in permutations(sorted(chars.upper()), int(comb))))