import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matrix A:")
print(A)

print("\nTranspose:")
print(A.T)

print("\nTrace:", np.trace(A))

print("\nRank:", np.linalg.matrix_rank(A))