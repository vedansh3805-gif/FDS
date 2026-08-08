import numpy as np

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
], dtype=float)

U, S, Vt = np.linalg.svd(A)

S_matrix = np.zeros_like(A)
np.fill_diagonal(S_matrix, S)

A_reconstructed = U @ S_matrix @ Vt

print("Original matrix A:")
print(A)

print("\nU:")
print(U)

print("\nSingular values:")
print(S)

print("\nVt:")
print(Vt)

print("\nReconstructed matrix:")
print(A_reconstructed)

print("\nReconstruction verified:",
      np.allclose(A, A_reconstructed))