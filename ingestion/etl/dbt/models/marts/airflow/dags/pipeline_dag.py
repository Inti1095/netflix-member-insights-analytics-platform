from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="netflix_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    ingest = BashOperator(
        task_id="generate_events",
        bash_command="python ingestion/generate_events.py"
    )

    etl = BashOperator(
        task_id="run_pyspark_etl",
        bash_command="python etl/pyspark_etl.py"
    )

    dbt_run = BashOperator(
        task_id="run_dbt",
        bash_command="cd dbt && dbt run"
    )

    ingest >> etl >> dbt_run
