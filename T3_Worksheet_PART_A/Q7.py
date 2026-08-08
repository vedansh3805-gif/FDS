import numpy as np

A = np.array([
    [1, 2],
    [2, 1],
    [3, 4],
    [4, 3]
])

b = np.array([5, 4, 10, 9])

A_pinv = np.linalg.pinv(A)

x = A_pinv @ b

print("Matrix A:")
print(A)

print("\nVector b:")
print(b)

print("\nPseudo-inverse of A:")
print(A_pinv)

print("\nLeast-squares solution x:")
print(x)

print("\nApproximation A @ x:")
print(A @ x)