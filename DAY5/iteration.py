import numpy as np 
 # for-in-loop
 #1D array
array_1D = np.array([1,2,3,4,5,6])
#iterate the elements in this array
print("Array_1D:",array_1D)

for elements in array_1D:
  print(elements)

array_2D = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print("2D array :",array_2D)

#iterate 2D array
for elements in array_2D:
  print(elements)

#iterate 2D array
#for rows in array_2D:
  #print(rows)

#for elements in row:
 # print(elements)  

for elements in np.nditer(array_2D):
  print(elements) 

#iterate the elements with index
for index,element in np.ndenumerate(array_2D):
  print(f"Index: {index},Element : {element}")

  