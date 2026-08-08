import numpy as np

np.random.seed(42)

samples = np.random.randn(1000)

mean = np.mean(samples)
std = np.std(samples)

print("Sample mean:", mean)
print("Sample standard deviation:", std)

print("\nMean approximately 0:", np.isclose(mean, 0, atol=0.1))
print("Standard deviation approximately 1:",
      np.isclose(std, 1, atol=0.1))