#Generates a 5x5 matrix with random integers between 10 and 50, then finds the minimum and maximum values in the matrix.

import numpy as np

matrix = np.random.randint(10, 51, size=(5, 5))
print("Matrix:\n", matrix)


min_val = matrix.min()
max_val = matrix.max()

print("Minimum value:", min_val)
print("Maximum value:", max_val)
