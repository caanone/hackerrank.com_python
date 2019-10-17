import numpy as np

n, m = list(map(int, input().split(" ")))
matrix_list = []

for _ in range(m):
    nMap = map(int, input().split(" "))
    matrix_list += [list(x for x in nMap if not None or not ' '), ]
    del nMap

print(np.prod(np.sum(matrix_list, axis=0)))








# my_array = np.array([[1, 2],
#                         [3, 4]])


# print(np.prod(my_array, axis=None))
# print(np.prod(my_array, axis=0))
# print(np.prod(my_array, axis=1))

"""
24
[3 8]
[ 2 12]
"""


