from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count

spark = (
    SparkSession.builder
    .appName("SilverToGold")
    .getOrCreate()
)

# Read Silver Layer
df = spark.read.parquet("silver_events")

print("Silver Records:", df.count())

# Gold Layer Aggregation
gold_df = (
    df.groupBy("event_type")
      .agg(
          count("*").alias("total_events"),
          sum("price").alias("total_revenue")
      )
)

gold_df.show()

# Save Gold Layer
gold_df.write.mode("overwrite").parquet("gold_metrics")

print("Gold layer created successfully")

spark.stop()