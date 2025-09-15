import random

def create_matrix(rows=3, cols=3):
    return [[random.randint(1, 9) for i in range(cols)] for i in range(rows)]

def sum_diagonal(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

matrix1 = create_matrix()
print("Matrix 1: ")
for row in matrix1:
    print(row)

print(f"Sum of diagonal elements: {sum_diagonal(matrix1)}")