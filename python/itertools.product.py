from itertools import product

aList, bList = set(), set()

aMap = map(int, input().split(" "))
aList = set(x for x in aMap if not None or not ' ' or x in aList)


bMap = map(int, input().split(" "))
bList = set(x for x in bMap if not None or not ' ' or x in bList)


if 0 < len(bList) < 30 and 0 < len(bList) < 30:
    SystemExit()

print(*list(product(aList, bList)))

