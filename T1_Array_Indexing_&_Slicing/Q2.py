import numpy as np

a = np.arange(1, 26).reshape(5, 5)

result = a[1:4, 1:4]

print("Original array:")
print(a)

print("\nMiddle 3x3 sub-matrix:")
print(result)