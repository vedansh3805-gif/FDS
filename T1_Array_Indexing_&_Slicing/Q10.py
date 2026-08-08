import numpy as np

arr = np.arange(24).reshape(2, 3, 4)

result = arr[:, :, 2]

print("Original 3D array:")
print(arr)

print("\n2D slice at depth index 2:")
print(result)