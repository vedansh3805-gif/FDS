import numpy as np

np.random.seed(42)

rolls = np.random.randint(1, 7, size=10000)

outcomes, counts = np.unique(rolls, return_counts=True)

frequencies = counts / len(rolls)

print("Outcome | Empirical Frequency | Theoretical Frequency")

for outcome, frequency in zip(outcomes, frequencies):
    print(
        outcome,
        "|",
        round(frequency, 4),
        "|",
        round(1 / 6, 4)
    )