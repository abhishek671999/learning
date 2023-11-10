from airflow import Dataset, DAG
from datetime import datetime

my_file = Dataset('temp_file.txt')

with DAG(
    dag_id='producer_dag',
    schedule='@daily',
    start_date=datetime(2023,1,11),
    catchup=False):
    
    @task(outlets=[my_file])
    def update_dataset():
        with open(my_file.uri, 'a+') as fp:
            fp.write('Hello there')
        
    update_dataset
