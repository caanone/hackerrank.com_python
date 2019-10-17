#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    capitalized = ""
    fullname = s.split(" ")
    for name in fullname:
        capitalized += name.capitalize() + " "
    print(capitalized)
    return capitalized


if __name__ == '__main__':
    # os.environ['OUTPUT_PATH'] = os.getcwd()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
