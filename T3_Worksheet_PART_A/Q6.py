import numpy as np

v = np.array([3, -4, 5])

l1_norm = np.linalg.norm(v, ord=1)
l2_norm = np.linalg.norm(v, ord=2)
inf_norm = np.linalg.norm(v, ord=np.inf)

print("Vector:")
print(v)

print("\nL1 norm:", l1_norm)
print("L2 norm:", l2_norm)
print("Infinity norm:", inf_norm)

# L1 norm -> sum of absolute values
# L2 norm -> Euclidean length
# Infinity norm -> maximum absolute value