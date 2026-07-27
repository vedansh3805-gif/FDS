import numpy as np

A = np.array([[12, 15, 18, 20],
              [25, 28, 30, 35],
              [40, 42, 45, 48]])

print("Original Array:")
print(A)

print("\nFirst Row:")
print(A[0])

print("\nLast Column:")
print(A[:, -1])

print("\nFirst Two Rows:")
print(A[:2])

print("\nSubarray (28,30,42,45):")
print(A[1:3, 1:3])

print("\nEvery Alternate Column:")
print(A[:, ::2])