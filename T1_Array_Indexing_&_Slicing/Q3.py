import numpy as np

a = np.arange(1, 26).reshape(5, 5)

result = a[-2:, :3]

print("Original array:")
print(a)

print("\nLast two rows and first three columns:")
print(result)