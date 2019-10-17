from itertools import combinations_with_replacement as cwr

if __name__ == "__main__":
    s, k = input().split(" ")
    k = int(k)
    if s.islower() or not 0 < k < len(s) +1:
        exit()
    s = sorted(list(s))
    for x in cwr(s, k):
        print(*x, sep="")