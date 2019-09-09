if __name__ == '__main__':
    n = int(input())
    mym = map(int, input().split(" "))
    myl = [x for x in mym if not None or not ' ']
    if len(myl) != n or not -100 <= len(myl) <= 100 or not 2 <= n <= 10:
        exit()
    myi = myl.sort(reverse=True)
    myd, i = {}, 1
    for x in myl:
        if [x] in myd.values() or x in myd.values() or [x, x] in myd.values() or [x, x, x] in myd.values() or [x, x, x, x] in myd.values() or [x, x, x, x, x] in myd.values()or [x, x, x, x, x, x] in myd.values() or [x, x, x, x, x, x, x] in myd.values() or [x, x, x, x, x, x, x, x] in myd.values() or [x, x, x, x, x, x, x, x, x] in myd.values():
            i -= 1
            myd[i] += [x, ]
            i += 1
        else:
            myd[i] = [x, ]
            i += 1
    if len(myd[2]) > 1:
        print(myd[2][1])
    else:
        print(*myd[2])
