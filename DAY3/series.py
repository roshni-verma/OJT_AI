import pandas as pd

#serires: which one dimentional.
data =[10,2,3,45,65]
series = pd.Series(data)
print(series)

#ACCESS THE ELEMENT SEPERATELY BY USING INDEXING

print (series[3])

#arithmatical operation 

series_add = series + 10
print(series_add)

#filter elements in the series.

filtered_series = series[series>20]
print(filtered_series)

#statical method
#data = [10,2,3,45,65]

mean = series.mean()
print (f"the mean value of the series is {mean}")