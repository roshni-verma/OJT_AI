# converting 1D into 2D
#.reshape () is the method which is used for reshaping the arrays.

import numpy as np

# create a 1D Array
array_1D = np.array([1,2,3,4,5,6])
print("array1D :",array_1D)
print("shape of array1D :",array_1D.shape)

#reshape the 1D array to 2D array
array_2D = array_1D.reshape((2,3))
print("2D array :",array_2D)
print("shape of array2D :",array_2D.shape)

#reshape 1D array into 3D 
array_3D = array_1D.reshape(3,2)
print("3D array:", array_3D)
print("shape of array3D :",array_3D.shape)

# reshape back a 2D array to 1D
array_1D_back = array_2D.reshape(1,6)
print("array_1D_back :",array_1D_back)
print("shape of array_1D_back :",array_1D_back.shape)


