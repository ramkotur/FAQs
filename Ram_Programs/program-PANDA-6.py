import pandas as pd

data = {'ename': ['aa', 'bb', 'cc', 'dd', 'ee'],
'dept': [10, 20, 10, 20, 10],
'sal': [100, 200, 300, 150, 250]}

df = pd.DataFrame(data)

d = df.groupby('dept')['sal'].sum().reset_index()

print(d)

# Group by dept and calculate the sum of sal and count of records for each dept
grouped_df = df.groupby('dept').agg({'sal': 'sum', 'ename': 'count'}).reset_index()

# Rename columns for clarity
grouped_df.rename(columns={'ename': 'count'}, inplace=True)

print(grouped_df)

df1 = grouped_df[grouped_df['count']>1].reset_index(drop=True)

print(df1)

#second_highest_salary = df.groupby('dept')['sal'].nlargest(2).groupby('dept').nth(1).reset_index()

second_highest_salary = df.groupby('dept')['sal'].nlargest(2)

print(second_highest_salary)
