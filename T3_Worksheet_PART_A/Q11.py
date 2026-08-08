import numpy as np

A = np.array([
    [1, 2],
    [2, 4.001]
])

condition_number = np.linalg.cond(A)

print("Matrix A:")
print(A)

print("\nCondition number:", condition_number)

if condition_number > 1000:
    print("\nLarge condition number: the system may be numerically sensitive.")
else:
    print("\nCondition number is not extremely large.")