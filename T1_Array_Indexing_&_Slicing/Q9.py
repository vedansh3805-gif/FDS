import numpy as np

arr = np.array([10, -5, 20, -8, 30, -2, 40])

arr[arr < 0] = 0

print("Array after replacing negative values with 0:")
print(arr)