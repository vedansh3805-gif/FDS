import numpy as np

A = np.arange(1, 25)

print("Original Array:")
print(A)

matrix1 = A.reshape(4, 6)
print("\n4 × 6 Matrix:")
print(matrix1)

matrix2 = A.reshape(2, 12)
print("\n2 × 12 Matrix:")
print(matrix2)

print("\nFlattened Array:")
print(matrix1.flatten())

print("\nTranspose of 4 × 6 Matrix:")
print(matrix1.T)