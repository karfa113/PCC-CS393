import numpy as np

A = np.random.randint(1, 11, (3, 3))
print("Matrix A: \n", A)

row_max = np.max(A, axis=1)
col_min = np.min(A, axis=0)

print(f"Row-wise maximum: {row_max}")
print(f"Column-wise minimum: {col_min}")