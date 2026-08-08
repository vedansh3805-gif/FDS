import numpy as np

np.random.seed(42)

samples = np.random.normal(
    loc=50,
    scale=5,
    size=1000
)

mean = np.mean(samples)
std = np.std(samples)

lower = mean - std
upper = mean + std

within_one_std = np.sum(
    (samples >= lower) & (samples <= upper)
)

percentage = (within_one_std / len(samples)) * 100

print("Sample mean:", mean)
print("Sample standard deviation:", std)

print("\nRange:", lower, "to", upper)

print("\nSamples within one standard deviation:",
      within_one_std)

print("Percentage:", percentage, "%")

print("\nExpected percentage is roughly 68%.")