import numpy as np

arr = np.array([1, 2, 3, 4, 5])

cumulative_sum = np.cumsum(arr)
cumulative_product = np.cumprod(arr)

print("Original array:")
print(arr)

print("\nCumulative sum:")
print(cumulative_sum)

print("\nCumulative product:")
print(cumulative_product)