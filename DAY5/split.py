import numpy as np 
# split will works in  numpy 
array_1D=np.array([1,2,3,4,5,6])
spilt_array=np.split(array_1D,3)
print(spilt_array)
array = np.array([1,2,3,4,5,6,7,8,9])

split_array = np.split(array,3)
print("original array:",array)
print("split array :",split_array)

#multi dementional
#horizontally and vertically

array_1D =np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

vsplit_array = np.hsplit(array_1D,3)

print("vsplited array:", vsplit_array)

