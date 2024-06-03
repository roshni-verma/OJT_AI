#Find the number of rows and columns of a given matrix using NumPy
import numpy as np

# Given matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Get the shape of the matrix
num_rows, num_columns = matrix.shape

print("Number of Rows:", num_rows)
print("Number of Columns:", num_columns)
