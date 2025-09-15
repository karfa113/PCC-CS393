import random

complex_matrix1 = [[complex(random.randint(1, 5), random.randint(1, 5)) for i in range(3)] for j in range(3)]
complex_matrix2 = [[complex(random.randint(1, 5), random.randint(1, 5)) for i in range(3)] for j in range(3)]

def complex_add(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(3)] for i in range(3)]

def complex_sub(m1, m2):
    return [[m1[i][j] - m2[i][j] for j in range(3)] for i in range(3)]

def complex_mul(m1, m2):
    result = [[0+0j]*3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

print("Complex Matrix 1: ")
for row in complex_matrix1:
    print(row)

print("Complex Matrix 2: ")
for row in complex_matrix2:
    print(row)

print("Addition: ")
for row in complex_add(complex_matrix1, complex_matrix2):
    print(row)

print("Subtraction: ")
for row in complex_sub(complex_matrix1, complex_matrix2):
    print(row)

print("Multiplication: ")
for row in complex_mul(complex_matrix1, complex_matrix2):
    print(row)