import random

def create_matrix(rows=3, cols=3):
    return [[random.randint(1, 9) for i in range(cols)] for i in range(rows)]

def row_max(matrix):
    return [max(row) for row in matrix]

def col_min(matrix):
    return [min(matrix[i][j] for i in range(3)) for j in range(3)]

matrix1 = create_matrix()
print("Matrix 1: ")
for row in matrix1:
    print(row)

print(f"Row-wise maximum: {row_max(matrix1)}")
print(f"Column-wise minimum: {col_min(matrix1)}")