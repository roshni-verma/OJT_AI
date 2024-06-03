#Adding and Subtracting Matrices in Python.
import numpy as np

# Define two matrices
matrix_A = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matrix_B = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# Add the matrices
sum_matrix = matrix_A + matrix_B

# Subtract the matrices
difference_matrix = matrix_A - matrix_B

# Print the results
print("Sum of matrices:")
print(sum_matrix)

print("Difference of matrices:")
print(difference_matrix)
