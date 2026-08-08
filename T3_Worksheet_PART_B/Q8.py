import numpy as np

np.random.seed(42)

dataset = np.arange(30).reshape(10, 3)

print("Original dataset:")
print(dataset)

np.random.shuffle(dataset)

print("\nShuffled dataset:")
print(dataset)

# np.random.shuffle() shuffles rows of a 2D array.
# The elements within each row remain together.