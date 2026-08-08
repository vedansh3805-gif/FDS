import numpy as np

np.random.seed(42)

samples = np.random.binomial(
    n=10,
    p=0.5,
    size=1000
)

empirical_mean = np.mean(samples)

theoretical_mean = 10 * 0.5

print("Empirical mean:", empirical_mean)
print("Theoretical mean:", theoretical_mean)

print("\nDifference:",
      abs(empirical_mean - theoretical_mean))