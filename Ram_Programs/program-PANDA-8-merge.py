import pandas as pd

df1= {
    'key': ['A', 'B', 'C', 'D'],
    'value': [1, 2, 3, 4]
}

df2 = {
    'key': ['B', 'D', 'E', 'F'],
    'value': [5, 6, 7, 8]
}

# Create sample DataFrames
df1 = pd.DataFrame(df1)
df2 = pd.DataFrame(df2)

# Merge DataFrames on the 'key' column
merged_df = pd.merge(df1, df2, on='key', how='inner', suffixes=('_df1', '_df2'))

print(merged_df)
