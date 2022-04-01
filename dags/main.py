from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Sahil Seli',
    'start_date': datetime(2022, 3, 30),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG('Docker-Kubernetes_Assignment', default_args=default_args, schedule_interval='@daily', template_searchpath=['/usr/local/airflow/sql_files'], catchup=False) as dag:

    task0 = DummyOperator(task_id="initiated")
    task1 = PostgresOperator(task_id='log_details_upload', postgres_conn_id='postgres_conn', sql='create_table.sql')
    task0 >> task1