#Matrix Multiplication in NumPy
import numpy as np

# Define two matrices
matrix_A = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matrix_B = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# Multiply matrices using numpy.dot()
result_dot = np.dot(matrix_A, matrix_B)

# Multiply matrices using the @ operator
result_at = matrix_A @ matrix_B

print(result_dot, result_at)
