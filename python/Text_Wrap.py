# Accepted Solution
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


##########################################################
# # Must be ...

import textwrap as tw

def wrap(string, max_width):
    return tw.wrap(string, max_width)

if __name__ == '__main__':
    string = str(input())
    width = int(input())
    if not 0 < len(string) < 10**3 and not 0 < width < len(string):
        SystemExit()
    for _ in wrap(string, width):
        print(_, sep="\n")
