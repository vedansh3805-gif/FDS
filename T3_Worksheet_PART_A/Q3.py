import numpy as np

A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

b = np.array([8, -11, -3])

x = np.linalg.solve(A, b)

print("Solution [x, y, z]:")
print(x)

print("\nSubstitution result A @ x:")
print(A @ x)

print("\nOriginal b:")
print(b)

print("\nSolution verified:",
      np.allclose(A @ x, b))