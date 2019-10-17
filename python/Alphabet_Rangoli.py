def print_rangoli(size):
    chars = "abcdefghijklmnopqrstuvwxyz"
    for x, y in size * 2 - 1:
        pass
    print(chars[:size])


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)