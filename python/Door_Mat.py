n, m = list(map(int, input().split(" ")))
if m / 3 != n and m > 0 and m % 2 != 0:
    SystemExit()
for i in range(1, n, 2):
    print(str('.|.' * i).center(m, '-'))
print('WELCOME'.center(m, "-"))
for i in range(n-2, -1, -2):
    print(str('.|.' * i).center(m, '-'))
