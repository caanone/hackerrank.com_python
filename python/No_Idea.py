n, m = (int(i) for i in input().split())

l = map(int, input().strip().split(' '))

a = set(map(int, input().strip().split(' ')))

b = set(map(int, input().strip().split(' ')))

res = 0

for x in l:
    if x in a:
        res += 1
    if x in b:
        res += -1

print(res)