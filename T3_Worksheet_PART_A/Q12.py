import numpy as np

A = np.array([
    [4, 2, 1],
    [2, 3, 0],
    [1, 0, 2]
])

eigenvalues = np.linalg.eigvalsh(A)

print("Symmetric matrix:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nAll eigenvalues are non-negative:",
      np.all(eigenvalues >= 0))