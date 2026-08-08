import numpy as np

# Legacy global random state
np.random.seed(42)
legacy_integers = np.random.randint(1, 101, size=10)

# New Generator API
rng = np.random.default_rng(42)
generator_integers = rng.integers(1, 101, size=10)

print("Using np.random.seed() + randint():")
print(legacy_integers)

print("\nUsing default_rng() + integers():")
print(generator_integers)

print("\nBoth generate 10 random integers.")

# default_rng() is recommended for new code because
# it provides an independent Generator object and
# avoids relying on global random state.