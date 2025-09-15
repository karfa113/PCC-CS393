import random

def create_matrix(rows=3, cols=3):
    return [[random.randint(1, 9) for i in range(cols)] for i in range(rows)]

def elementwise_multiply(m1, m2):
    return [[matrix1[i][j] * matrix2[i][j] for j in range(3)] for i in range(3)]

matrix1 = create_matrix()
print("Matrix 1: ")
for row in matrix1:
    print(row)

matrix2 = create_matrix()
print("Matrix 2: ")
for row in matrix2:
    print(row)

elementwise_product = elementwise_multiply(matrix1, matrix2)
print("Element-wise multiplication: ")
for row in elementwise_product:
    print(row)