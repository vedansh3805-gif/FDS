import numpy as np

A = np.array([
    [2, 1, 0],
    [0, 3, 1],
    [1, 0, 4]
])

eigenvalues = np.linalg.eigvals(A)

trace_A = np.trace(A)
det_A = np.linalg.det(A)

sum_eigenvalues = np.sum(eigenvalues)
product_eigenvalues = np.prod(eigenvalues)

print("Matrix A:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nTrace:", trace_A)
print("Sum of eigenvalues:", sum_eigenvalues)

print("\nDeterminant:", det_A)
print("Product of eigenvalues:", product_eigenvalues)

print("\nTrace verified:",
      np.allclose(trace_A, sum_eigenvalues))

print("Determinant verified:",
      np.allclose(det_A, product_eigenvalues))