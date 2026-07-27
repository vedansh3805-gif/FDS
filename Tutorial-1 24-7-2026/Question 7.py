import numpy as np

print("5 × 5 Identity Matrix:")
print(np.identity(5))

print("\n5 × 5 Matrix using eye():")
print(np.eye(5))

print("\nMatrix with Ones on First Upper Diagonal:")
print(np.eye(5, k=1))

print("\nComparison:")
print("identity() creates only a square identity matrix.")
print("eye() can create identity-like matrices with shifted diagonals using k.")