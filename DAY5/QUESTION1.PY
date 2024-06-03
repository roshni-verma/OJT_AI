#Counts the number of non-zero values in the array
import numpy as np

# Example array
array = np.array([[1, 0, 3],
                  [0, 5, 0],
                  [7, 8, 0]])

# Count the number of non-zero values
non_zero_count = np.count_nonzero(array)

print("Number of non-zero values:", non_zero_count)
