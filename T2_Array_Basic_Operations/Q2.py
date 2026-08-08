import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

dot_product = np.dot(a, b)
matrix_product = a @ b

print("Dot product:")
print(dot_product)

print("\nMatrix product using @:")
print(matrix_product)

print("\nAre they equal?", np.array_equal(dot_product, matrix_product))

# For 2D arrays, np.dot() and @ perform matrix multiplication,
# so they give the same result.
# Their behavior differs for higher-dimensional arrays.