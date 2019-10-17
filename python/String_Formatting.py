def print_formatted(number):

    for i in range(1, number+1):
        print("{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}".format(i, w=len(bin(number)[2:])))

    # # Detailed version added below:
    # widthofbin = len(str(bin(number)).replace('0b', ''))
    # for x in range(1, number + 1):
    #     decx = str(x).rjust(widthofbin, ' ')
    #     octx = str(oct(x)).split("o")[1].rjust(widthofbin, ' ')
    #     hexx = str(hex(x)).split("x")[1].upper().rjust(widthofbin, ' ')
    #     binx = str(bin(x)).split("b")[1].rjust(widthofbin, ' ')
    #     print(decx, octx, hexx, binx)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
