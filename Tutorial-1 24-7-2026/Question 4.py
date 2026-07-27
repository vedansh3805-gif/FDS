import numpy as np

A = np.array([45, 12, 78, 25, 56, 12, 34, 78])

print("Original Array:")
print(A)

print("\nIndex of first occurrence of 12:")
print(np.where(A == 12)[0][0])

print("\nAll indices of 78:")
print(np.where(A == 78)[0])

print("\nAscending Order:")
print(np.sort(A))

print("\nDescending Order:")
print(np.sort(A)[::-1])