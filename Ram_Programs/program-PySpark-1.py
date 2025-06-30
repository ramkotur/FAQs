from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder.appName("DuplicateAges").getOrCreate()

data = [('aa', 10), ('bb', 20), ('cc', 10)]
columns = ['name', 'age']

df = spark.createDataFrame(data, columns)

# Find duplicate ages
duplicate_ages = df.groupBy("age").count().filter(col("count") > 1).select("age")

duplicate_ages.show()

# Join to get the names with duplicate ages
result = df.join(duplicate_ages, on="age", how="inner")

result.show()
