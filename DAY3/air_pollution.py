import pandas as pd

# Read CSV file into DataFrame
df = pd.read_csv('air-pollution.csv')

# Check the unique countries
unique_countries = df['Entity'].unique()
print("All countries:", unique_countries)

df_filled_data = df.fillna(0)

print(df_filled_data)



df_duplicated_data = pd.read_csv('air-pollution.csv')

print(df_duplicated_data.duplicated())

