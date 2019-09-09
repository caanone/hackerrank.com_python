import numpy as np

n, m = list(map(int, input().split(" ")))
matrix_list = []
for _ in range(n):
    nMap = map(int, input().split(" "))
    matrix_list += [list(x for x in nMap if not None or not ' '), ]
result_array = np.max(np.min(matrix_list, axis=1))
print(result_array)
del result_array, matrix_list, n, m
