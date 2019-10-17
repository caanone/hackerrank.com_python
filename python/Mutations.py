def mutate_string(*args) -> str:
    position = int(args[1])
    return args[0][:position] + args[2] + args[0][position + 1:]


if __name__ == '__main__':
    print(mutate_string(input(), *input().split(" ")))



# Accepted solution added below:

"""
def mutate_string(string, position, character):
    position = int(args[1])
    return args[0][:position] + args[2] + args[0][position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

"""