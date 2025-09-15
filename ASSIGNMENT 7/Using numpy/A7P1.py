import numpy as np

matrix = np.random.randint(1, 11, (3, 3))
print("matrix: \n", matrix)

diagonal_sum = np.trace(matrix)
print(f"Sum of diagonal elements: {diagonal_sum}")