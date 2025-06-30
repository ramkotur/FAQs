import csv

# Create a list of dictionaries to represent the dataset
data = [
    {'Name': 'Alice', 'Age': 29, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 31, 'City': 'Los Angeles'},
    {'Name': 'Cathy', 'Age': 25, 'City': 'Chicago'},
    {'Name': 'David', 'Age': 35, 'City': 'Houston'}
]

# Display the dataset
print("Dataset:")
for row in data:
    print(row)

# Filter rows where Age is greater than 30
filtered_data = [row for row in data if row['Age'] > 30]
print("\nFiltered Dataset (Age > 30):")
for row in filtered_data:
    print(row)

# Group by City and count the number of people in each city
city_count = {}
for row in data:
    city = row['City']
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print("\nGrouped Dataset (Count by City):")
for city, count in city_count.items():
    print(f"{city}: {count}")

# Save the dataset to a CSV file
with open('people.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

print("\nDataset saved to 'people1.csv'")