# Count the occurrence of each element from a list. Write a program that a given list count the occurrence of each element
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("ElementCount").getOrCreate()

# Sample list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

# Create RDD from the list
rdd = spark.sparkContext.parallelize(sample_list)

# Map each element to a (key, 1) pair and reduce by key to count occurrences
element_counts = rdd.map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)

# Collect and print the result
result = element_counts.collect()
print(dict(result))

# Stop the Spark session
spark.stop()
