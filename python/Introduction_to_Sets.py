def average(array: list):
    array = set(array)
    cum = 0
    for x in array: cum += x
    return cum / len(array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    