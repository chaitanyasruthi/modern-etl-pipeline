from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

spark = (
    SparkSession.builder
    .appName("BronzeToSilver")
    .getOrCreate()
)

df = spark.read.json("raw_events.jsonl")

print("Bronze Count:", df.count())

df_clean = (
    df.dropna()
      .filter(col("price") > 0)
      .withColumn("timestamp", to_timestamp(col("timestamp")))
)

print("Silver Count:", df_clean.count())

df_clean.write.mode("overwrite").parquet("silver_events")

print("Silver parquet created")

spark.stop()