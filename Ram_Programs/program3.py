from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder.appName("HelloPySpark").getOrCreate()

# Create a DataFrame
data = [("Hello",), ("PySpark",)]
columns = ["Word"]
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()

# Stop the Spark session
spark.stop()