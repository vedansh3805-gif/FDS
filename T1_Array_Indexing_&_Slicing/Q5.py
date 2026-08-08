import numpy as np

arr = np.array([
    [10, 20, 5],
    [18, 12, 25],
    [30, 7, 16]
])

result = arr[arr > 15]

print("Original array:")
print(arr)

print("\nElements greater than 15:")
print(result)