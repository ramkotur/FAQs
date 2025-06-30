import pandas as pd

# Create sample DataFrames
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value': [1, 2, 3, 4]
}).set_index('key')

df2 = pd.DataFrame({
    'key': ['B', 'D', 'E', 'F'],
    'value': [5, 6, 7, 8]
}).set_index('key')

# Join DataFrames on the index
joined_df = df1.join(df2, how='inner', lsuffix='_df1', rsuffix='_df2')

print(joined_df)
