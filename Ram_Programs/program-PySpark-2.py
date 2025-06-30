from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("SQLExample").getOrCreate()

# Create a sample DataFrame
data = [('aa', 10, 100), ('bb', 20, 200), ('cc', 10, 300)]
columns = ['ename', 'dept', 'sal']

df = spark.createDataFrame(data, columns)

# Register the DataFrame as a temporary SQL table
df.createOrReplaceTempView("employees")

# Write and execute an SQL query
result = spark.sql("""
                SELECT dept, SUM(sal) AS total_sal
                FROM employees
                GROUP BY dept """)

result.show()
