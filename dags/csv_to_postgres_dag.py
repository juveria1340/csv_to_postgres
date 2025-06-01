from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
import pandas as pd

def load_csv_to_postgres():
    df = pd.read_csv('/opt/airflow/data/sample_bitcoin.csv')
    hook = PostgresHook(postgres_conn_id='postgres_default')
    engine = hook.get_sqlalchemy_engine()
    df.to_sql('your_table', engine, if_exists='replace', index=False)

with DAG('csv_to_postgres',
         start_date=datetime(2025, 1, 1),
         schedule_interval='@daily',
         catchup=False) as dag:

    load_task = PythonOperator(
        task_id='load_csv',
        python_callable=load_csv_to_postgres,
        execution_timeout=timedelta(minutes=60)
    )
