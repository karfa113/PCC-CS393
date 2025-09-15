import numpy as np

A = np.random.randint(1, 11, (3, 3))
B = np.random.randint(1, 11, (3, 3))
result = np.dot(A, B)

print("Matrix A: \n", A)
print("Matrix B: \n", B)
print("Matrix multiplication: \n", result)