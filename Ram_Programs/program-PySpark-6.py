#------------RDD ---------------

from pyspark import SparkContext

# Use the existing SparkContext provided by Databricks
sc = spark.sparkContext

# Create an RDD from a list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Collect and print the RDD contents
rdd_output = rdd.collect()
print(rdd_output)

