"""https://projecteuler.net/problem=16

2 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 1000?   

"""


def get_problem_wants_what(numeros: int, le_power_of: int):
    a = pow(numeros, le_power_of)
    b = 0
    for x in str(a):
        b += int(x)
    return b


def get_problem_wants_what_with_different_way(numeros: int, le_power_of: int):
    a = pow(numeros, le_power_of)
    print(f"a is {a}")
    b, i = 0, 1
    while a > 0:
        b += (a % 10)
        a = int(a / 10)

    # for x in range(len(str(a))):
    #     b = b + (a % 10**(x+1)) 
    #     print(b)
    #     i += 1
    return b

x = 95
print(get_problem_wants_what_with_different_way(2, x))
print(get_problem_wants_what(2, x))
