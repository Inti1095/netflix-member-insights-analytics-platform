from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

spark = SparkSession.builder.appName("NetflixETL").getOrCreate()

df = spark.read.json("data/raw/events.json")

clean_df = (
    df.withColumn("timestamp", to_timestamp(col("timestamp")))
      .filter(col("user_id").isNotNull())
)

clean_df.write.mode("overwrite").parquet("data/processed/events")
