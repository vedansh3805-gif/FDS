import numpy as np

np.random.seed(42)

dataset = np.arange(100)

indices = np.random.permutation(len(dataset))

train_size = int(0.8 * len(dataset))

train_indices = indices[:train_size]
test_indices = indices[train_size:]

train_data = dataset[train_indices]
test_data = dataset[test_indices]

print("Training data:")
print(train_data)

print("\nTraining size:", len(train_data))

print("\nTesting data:")
print(test_data)

print("\nTesting size:", len(test_data))