import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

vertical = np.vstack((a, b))
horizontal = np.hstack((a, b))

print("Array A:")
print(a)

print("\nArray B:")
print(b)

print("\nVertical concatenation:")
print(vertical)

print("\nHorizontal concatenation:")
print(horizontal)