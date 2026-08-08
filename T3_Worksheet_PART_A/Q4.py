import numpy as np

A = np.array([
    [2, 1, 0],
    [1, 2, 1],
    [0, 1, 2]
])

eigenvalues, eigenvectors = np.linalg.eigh(A)

print("Matrix A:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# Select the first eigenvalue-eigenvector pair
lam = eigenvalues[0]
v = eigenvectors[:, 0]

print("\nSelected eigenvalue:")
print(lam)

print("\nSelected eigenvector:")
print(v)

print("\nA @ v:")
print(A @ v)

print("\nλ * v:")
print(lam * v)

print("\nVerified:",
      np.allclose(A @ v, lam * v))