import numpy as np

A = np.array([
    [4, 2],
    [1, 3]
])

det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)

print("Matrix A:")
print(A)

print("\nDeterminant:", det_A)

print("\nInverse:")
print(inv_A)

print("\nA @ inv(A):")
print(A @ inv_A)

print("\nApproximately identity:",
      np.allclose(A @ inv_A, np.eye(2)))