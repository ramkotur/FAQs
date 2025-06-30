import pandas as pd
df = pd.read_csv('file.csv')
print(df.head())


# What is the difference between loc and iloc in pandas?

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df.loc[0])  # Access by label
print(df.iloc[0])  # Access by integer location
