import copy

a = [0] * 4
b = [a for i in range(4)]
matrix = copy.deepcopy([[0] * 4]) * 4
matrix2 = [[0] * 4] * 4

matrix[0][0] = 3
matrix2[0][0] = 3
b[0][0] = 3

print(matrix)
print(matrix2)
print(b)

## Solution
works = [([0]*4).copy() for i in range(4)]
works = [([0]*4)[:] for i in range(4)]
works[0][0] = 3
print(works)
