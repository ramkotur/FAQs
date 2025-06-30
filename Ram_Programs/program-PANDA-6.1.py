import pandas as pd

# Creating the data dictionary
data = {
    'name': ['aa', 'bb', 'cc'],
    'dept': [10, 20, 10],
    'sal': [100, 200, 100]
}

# Converting the dictionary to a DataFrame
df = pd.DataFrame(data)

# Grouping by 'dept', then aggregating 'sal' with sum and counting 'dept'
d = df.groupby(['dept']).agg({'sal': 'sum', 'dept': 'count'})

# Renaming the count column to avoid conflict
d.rename(columns={'dept': 'dept_count','name':'name_count'}, inplace=True)

# Resetting the index
d = d.reset_index()

# Filtering the DataFrame where 'dept_count' is greater than 1
d = d[d['dept_count'] > 1]

# Printing the result
print(d)
