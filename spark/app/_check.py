from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, avg

import sys
import datetime

if __name__ == "__main__":
    # Create a SparkSession
    spark = SparkSession.builder \
    .master("local[*]") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio1:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "kirihara") \
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()


    df_silver = spark.read \
        .format("parquet") \
        .load("s3a://cken-coins-data/silver/delta_table/price_coins_follow_minute")
    print("no_rows_in_silver_layer:{}".format(df_silver.count()))
    df_silver.show()
    #no_rows_in_silver_layer:200

    
    df_minute = spark.read \
        .format("parquet") \
        .load("s3a://cken-coins-data/gold/fact/fact_minute_price")
    print("no_rows_in_minute:{}".format(df_minute.count()))
    df_minute.show()
    # no_rows_in_minute:500

    df_hour = spark.read \
        .format("parquet") \
        .load("s3a://cken-coins-data/gold/fact/fact_hour_price")
    print("no_rows_in_hour:{}".format(df_hour.count()))
    df_hour.show()
    #no_rows_in_hour:100

    df_day = spark.read \
        .format("parquet") \
        .load("s3a://cken-coins-data/gold/fact/fact_day_price")
    print("no_rows_in_day:{}".format(df_day.count()))
    df_day.show()