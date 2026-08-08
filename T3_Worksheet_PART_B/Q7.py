import numpy as np

np.random.seed(42)

categories = np.array(["A", "B", "C"])
probabilities = [0.1, 0.2, 0.7]

draws = np.random.choice(
    categories,
    size=1000,
    p=probabilities
)

values, counts = np.unique(draws, return_counts=True)

print("Category | Empirical Proportion | Theoretical Proportion")

for category, count in zip(values, counts):
    proportion = count / len(draws)

    theoretical = probabilities[
        np.where(categories == category)[0][0]
    ]

    print(
        category,
        "|",
        round(proportion, 3),
        "|",
        theoretical
    )