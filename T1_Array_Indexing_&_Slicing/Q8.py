import numpy as np

a = np.arange(1, 37).reshape(6, 6)

rows = [0, 2, 4]
columns = [1, 3, 5]

result = a[np.ix_(rows, columns)]

print("Original array:")
print(a)

print("\nSelected 3x3 array:")
print(result)