#Calculate the sum of the diagonal elements of a NumPy array 3*3 and 4*4

import numpy as np

# Define a 3x3 NumPy array
array_3x3 = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

# Define a 4x4 NumPy array
array_4x4 = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])

# Calculate the sum of diagonal elements for the 3x3 array
sum_diag_3x3 = np.sum(np.diagonal(array_3x3))

# Calculate the sum of diagonal elements for the 4x4 array
sum_diag_4x4 = np.sum(np.diagonal(array_4x4))

sum_diag_3x3, sum_diag_4x4
print("sum of the diagonal elements of a NumPy array 3*3: ",sum_diag_3x3)
print("sum of the diagonal elements of a NumPy array 4*4: ",sum_diag_4x4)