import numpy as np

arr = np.array([40, 10, 30, 20, 50])

sorted_arr = np.sort(arr)
sort_indices = np.argsort(arr)

print("Original array:")
print(arr)

print("\nSorted array:")
print(sorted_arr)

print("\nIndices that would sort the array:")
print(sort_indices)