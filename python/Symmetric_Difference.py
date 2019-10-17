
if __name__ == "__main__":
    aC = int(input())
    a = set()
    a.update(input().split(" "))
    aL = list()

    bC = int(input())
    b = set()
    b.update(input().split(" "))
    bL = list()

    # not accepting with fllowing comment block
    # if aC != len(a) or bC != len(b):
    #     exit()
    

    for x in sorted([int(x) for x in a.difference(b)]):
        aL += [x]
    aL = sorted(aL)
    for x in sorted([int(x) for x in b.difference(a)]):
        bL += [x]
    bL = sorted(bL)
    sum_L = aL + bL
    
    print(*sorted(sum_L), sep="\n")


    # different perspective :)
    # print(*sorted(list(a.symmetric_difference(b))),sep="\n")
