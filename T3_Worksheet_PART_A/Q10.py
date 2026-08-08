import numpy as np

vectors = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [1, 0, 1]
])

rank = np.linalg.matrix_rank(vectors)

print("Matrix of vectors:")
print(vectors)

print("\nRank:", rank)

if rank == len(vectors):
    print("The vectors are linearly independent.")
else:
    print("The vectors are linearly dependent.")