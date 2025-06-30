
# Count the occurrence of each element from a list. Write a program that a given list count the occurrence of each element
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

# Create an empty dictionary to store counts
element_counts = {}

# Count each element
for item in sample_list:
    if item in element_counts:
        element_counts[item] += 1
    else:
        element_counts[item] = 1

# Print the result
print(element_counts)
