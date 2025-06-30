from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Program2") \
    .master("local[*]") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()

# Create a sample DataFrame
data = [
    ("Alice", "2021-01-01", 1000),
    ("Bob", "2021-01-02", 1500),
    ("Alice", "2021-01-03", 2000),
    ("Bob", "2021-01-04", 2500),
]

print("------------Start--------------")


columns = ["Name", "Date", "Amount"]
df = spark.createDataFrame(data, schema=columns)

# Check the schema
df.printSchema()

# Show a sample of the DataFrame
df.show()


print("------------Its End--------------")

# Stop the Spark session
spark.stop()
