from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from pandas import json_normalize

import json
from datetime import datetime

def _process_user(ti):
    data = ti.xcom_pull(task_ids='extract_user')
    print('Extracted user: ', data)
    processed_data = json_normalize({
        'origin_ip': data['origin']
    })
    processed_data.to_csv('/tmp/processed_data.csv', index=False, header=False)

with DAG('user_test_dag', start_date=datetime(2023, 1, 11), schedule_interval='@daily', catchup=False) as dag:
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgress',
        sql='''
            CREATE TABLE IF NOT EXIST users (
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            )
        '''
    )
    is_api_available = HttpSensor(
        task_id='is_api_available',
        http_conn_id='http_default',
        endpoint='/ip'
    )

    extract_user = SimpleHttpOperator(
        task_id='extract_user',
        http_conn_id='http_default',
        endpoint='/ip',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )
    process_user = PythonOperator(
        task_id='process_user',
        python_callable=_process_user
    )

    is_api_available >> extract_user >> process_user