from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("HelloWorld").getOrCreate()

# Create a DataFrame with a single column and a single row
data = [("Hello, World!",)]
df = spark.createDataFrame(data, ["message"])

# Show the DataFrame
df.show()

# Stop the Spark session
spark.stop()
