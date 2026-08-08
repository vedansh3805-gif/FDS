import numpy as np

arr = np.arange(1, 17).reshape(4, 4)

arr[0, :] = 0
arr[-1, :] = 0
arr[:, 0] = 0
arr[:, -1] = 0

print("Array after setting the border to 0:")
print(arr)