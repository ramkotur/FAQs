
# Import necessary libraries
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("ReadParquet").getOrCreate()

# Read the Parquet file from Databricks File System (DBFS)
df = spark.read.parquet("/dbfs/path/to/parquet/file")

# Show the data
df.show()
