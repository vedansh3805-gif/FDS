import numpy as np

np.random.seed(42)

items = np.arange(1, 21)

without_replacement = np.random.choice(
    items,
    size=5,
    replace=False
)

with_replacement = np.random.choice(
    items,
    size=5,
    replace=True
)

print("Original items:")
print(items)

print("\nWithout replacement:")
print(without_replacement)

print("\nWith replacement:")
print(with_replacement)

# Without replacement -> an item cannot be selected again.
# With replacement -> the same item can appear multiple times.