#dataframe is two dimentional which is in a tabular formate.

import pandas as pd 

#create a data frame with a dictionary
data = {
    'Name': ['kigini', 'tuttu','ikka'],
    'Age': [24,23,24],
    'place':['koovode','mavoor','punoor']
}

#convert the data into dataframes
df = pd.DataFrame(data)

#print(df)

#print(df['Name'])
#print(df[['Name','place']])

# for acessing each row the 
print(df[df['Age'] > 23])
#add a new column into the dataframe
df['stiphend']=[15000,5000,5000]
print(df)

#remove a  column 
df = df.drop(columns=['stiphend'])
print(df)

#statical function
#describe() help get the summary of statics of your data frame
print(df.describe())