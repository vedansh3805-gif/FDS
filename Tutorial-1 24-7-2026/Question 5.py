import numpy as np

A = np.array([10, 20, 30, 40])

copy_array = A.copy()
view_array = A.view()

print("Original Array:", A)

A[0] = 100

print("\nModified Original Array:", A)
print("Copy:", copy_array)
print("View:", view_array)

print("\nDifference:")
print("copy() creates a separate array.")
print("view() shares memory with the original array.")