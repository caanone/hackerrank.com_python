if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    great_tuple = ()
    for _ in integer_list:
        great_tuple += (_,)
    print(hash(great_tuple))
