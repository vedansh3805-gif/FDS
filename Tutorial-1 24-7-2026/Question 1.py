import numpy as np

# 1D Array
arr1 = np.array([10, 20, 30, 40, 50])

print("1D Array:", arr1)
print("Shape:", arr1.shape)
print("Dimensions:", arr1.ndim)
print("Size:", arr1.size)
print("Data Type:", arr1.dtype)

# 2D Array
arr2 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

print("\n2D Array:")
print(arr2)
print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)