import numpy as np

array = np.array([10,20,12,15,14,17])
#np.where(array ==20)
#where(): use to check the particular condition for filter and condition 

#element greater than 15 for the above array
elements = np.where(array>15)
print(array[elements])


#replacing with 0
elements = np.where(array>15,0,array)
print(elements)