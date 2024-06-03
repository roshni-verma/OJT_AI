#How to inverse a matrix using NumPy
import numpy as np

# Define a square matrix
matrix = np.array([[1, 2, 3],
                   [0, 1, 4],
                   [5, 6, 0]])

# Compute the inverse of the matrix
inverse_matrix = np.linalg.inv(matrix)

print(inverse_matrix)
