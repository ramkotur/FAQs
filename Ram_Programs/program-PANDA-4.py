
import pandas as pd
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Age': [25, 30]})
merged_df = pd.merge(df1, df2, on='ID')
print(merged_df)
