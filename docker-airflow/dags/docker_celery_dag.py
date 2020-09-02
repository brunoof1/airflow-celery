import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.postgres_operator import PostgresOperator

default_args = {
	'owner': 'airflow',
	'start_date': dt.datetime(2020, 8, 27, 11, 30, 00),
	'retries': 3
}

with DAG('docker_celery_dag',
	default_args=default_args,
	schedule_interval='*/5 * * * *',
	catchup=False) as dag:

	opr_end = BashOperator(task_id='opr_end', bash_command='echo "Done"')
