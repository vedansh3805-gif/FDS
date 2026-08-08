import numpy as np

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

B = np.array([
    [7, 8, 9, 10],
    [11, 12, 13, 14]
])

result = A @ B

print("Matrix A shape:", A.shape)
print("Matrix B shape:", B.shape)

print("\nA @ B:")
print(result)

print("\nResult shape:", result.shape)

# (m,n) @ (n,p) -> (m,p)
# Here: (3,2) @ (2,4) -> (3,4)