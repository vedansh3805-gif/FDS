import numpy as np

arr = np.arange(1, 13)

reshaped = arr.reshape(3, 4)

flattened = reshaped.flatten()

ravelled = reshaped.ravel()

print("Original 1D array:")
print(arr)

print("\nReshaped to (3,4):")
print(reshaped)

print("\nFlatten:")
print(flattened)

print("\nRavel:")
print(ravelled)

# reshape() changes the shape of an array.
# flatten() converts the array into 1D and returns a copy.
# ravel() converts the array into 1D and usually returns a view.