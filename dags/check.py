from airflow import DAG 
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

spark_master = "spark://spark:7077"
spark_app_name = "check"

with DAG("check", start_date=datetime(2023,1,1), schedule_interval="@once", catchup=False) as dag:
    start = DummyOperator(task_id='start')

    end = DummyOperator(task_id='end')

    check = SparkSubmitOperator(
        task_id="check",
        application="/usr/local/spark/app/_check.py", # Spark application path created in airflow and spark cluster
        name=spark_app_name,
        conn_id="spark_default",
        verbose=1,
        conf={"spark.master":spark_master},
        jars="/usr/local/spark/resources/jars/aws-java-sdk-bundle-1.11.972.jar,/usr/local/spark/resources/jars/hadoop-aws-3.3.1.jar"
    )

    start >> check >> end
