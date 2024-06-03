import numpy as np
#created an array([[1,2,3],[4,5,6]])
array_2D= np.array(
    [
        [1,2,3],#0 index
        [4,5,6]#1 index
        ]
        )
#accessing a single element
element = array_2D[1,2]
print("element at the index of [1,2]",element)

#Access by 2 row 
# : symbol refers to entire rows
row = array_2D[1:]
print("second row : ",row)

#Access by 2 row 
row = array_2D[0,:]
print("first row : ",row)

# Access the 2nd column
second_column = array_2D[:, 1]

print("Second Column:",second_column)

#slicing 
#access the subarray with row of 0 and 1, column of 1 and 2
slice_array = array_2D[0:2,1:3]
print("subarray : ",slice_array)