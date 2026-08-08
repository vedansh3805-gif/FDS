import numpy as np

np.random.seed(42)

samples = np.random.uniform(
    low=10,
    high=20,
    size=1000
)

sample_min = np.min(samples)
sample_max = np.max(samples)
sample_mean = np.mean(samples)

print("Sample minimum:", sample_min)
print("Sample maximum:", sample_max)
print("Sample mean:", sample_mean)

print("\nMinimum within [10, 20]:",
      10 <= sample_min <= 20)

print("Maximum within [10, 20]:",
      10 <= sample_max <= 20)

print("Mean close to 15:",
      np.isclose(sample_mean, 15, atol=0.5))