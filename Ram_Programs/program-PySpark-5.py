
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

# URL of the CSV file
csv_url = "https://example.com/path/to/your/csvfile.csv"

# Read the CSV file
df = spark.read.format("csv").option("header", "true").load(csv_url)
