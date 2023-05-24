import os

# Folder in minio
BRONZE_LAYER_PATH = "bronze/coin_market/minute_crawled_data/"
SILVER_LAYER_PATH = "silver/delta_table/"
GOLD_LAYER_PATH = "gold/"

# Info to login Minio
accessKey="kirihara"
secretKey="minioadmin"
endpoint="http://minio1:9000"

# Bucket name of minio
bucketName = "cken-coins-data"

# File name of flat file in silver layer on minio
flatFileSilver = "price_coins_follow_minute"

# File name of fact and dim table on minio
factPriceMinute = "fact_minute_price"
factPriceHour = "fact_hour_price"
factPriceDay = "fact_day_price"
dimSymbolFile = "dim_symbol"
dimDateFile = "dim_date"


# Folder on local
RAW_PATH = "./my_data/raw_data/"
CLEAN_PATH = "./my_data/clean_data/"
STAGE_PATH = "./my_data/stage_layer/"

# File on local
tempFile = "temp_file.csv"
tempFileParquet = "temp_file.parquet"