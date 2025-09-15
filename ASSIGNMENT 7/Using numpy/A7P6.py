import numpy as np

A = np.random.randint(1, 6, (3, 3)) + 1j * np.random.randint(1, 6, (3, 3))
B = np.random.randint(1, 6, (3, 3)) + 1j * np.random.randint(1, 6, (3, 3))

add = A + B
sub = A - B
mul = np.dot(A, B)

print(f"Matrix A: \n{A}")
print(f"Matrix B: \n{B}")
print(f"Addition: \n{add}")
print(f"Subtraction: \n{sub}")
print(f"Multiplication: \n{mul}")