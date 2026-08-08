import numpy as np

a = np.arange(1, 26).reshape(5, 5)

sum_axis_0 = np.sum(a, axis=0)
sum_axis_1 = np.sum(a, axis=1)

print("Original array:")
print(a)

print("\nSum along axis=0:")
print(sum_axis_0)

print("\nSum along axis=1:")
print(sum_axis_1)

# axis=0 -> sums down the rows, giving column sums
# axis=1 -> sums across the columns, giving row sums