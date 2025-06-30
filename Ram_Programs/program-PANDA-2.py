import pandas as pd

# Create a dictionary of data
data = {
    'Name': ['Alice', 'Bob', 'Cathy', 'David'],
    'Age': [29, 31, 25, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)


filtered_df = df[df['Age'] > 30]

print(filtered_df)

# Group by City and count the number of people in each city

grouped_df = df.groupby('City').size().reset_index(name='Count')

print("\nGrouped DataFrame (Count by City):")
print(grouped_df)

# Save the DataFrame to a CSV file
df.to_csv('people.csv', index=False)
print("\nDataFrame saved to 'people.csv'")