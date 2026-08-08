import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

b = np.array([10, 20, 30])

result = a + b

print("Original array:")
print(a)

print("\nArray being broadcast:")
print(b)

print("\nResult:")
print(result)

# Shape of a = (4, 3)
# Shape of b = (3,)
# The dimensions are compatible because the last dimensions match.