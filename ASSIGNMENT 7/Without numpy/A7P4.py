import random

def create_matrix(rows=3, cols=3):
    return [[random.randint(1, 9) for i in range(cols)] for i in range(rows)]

def matrix_multiply(m1, m2):
    result = [[0]*3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

matrix1 = create_matrix()
print("Matrix 1: ")
for row in matrix1:
    print(row)

matrix2 = create_matrix()
print("Matrix 2: ")
for row in matrix2:
    print(row)

mul_result = matrix_multiply(matrix1, matrix2)
print(f"Matrix multiplication: ")
for row in mul_result:
    print(row)