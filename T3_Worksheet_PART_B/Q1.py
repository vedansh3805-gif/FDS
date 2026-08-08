import numpy as np

np.random.seed(42)
first = np.random.rand(10)

np.random.seed(42)
second = np.random.rand(10)

print("First generation:")
print(first)

print("\nSecond generation:")
print(second)

print("\nOutputs are identical:",
      np.array_equal(first, second))