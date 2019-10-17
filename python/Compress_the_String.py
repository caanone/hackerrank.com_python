from itertools import groupby

if __name__ == "__main__":
    string = input()
    for k, g in groupby(string):
        print((len(list(g)), int(k)), sep=" ", end=" ")