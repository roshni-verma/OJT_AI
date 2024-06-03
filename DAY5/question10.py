# How to count the frequency of unique values in NumPy array?
import numpy as np

# Define a NumPy array
array = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Get the unique values and their frequencies
unique_values, counts = np.unique(array, return_counts=True)

# Print the results
print("Unique values:", unique_values)
print("Counts:", counts)
