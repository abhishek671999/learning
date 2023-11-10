from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
import group_tasks.group_downloads as gd


with DAG('task_grouped_dag', start_date=datetime(2023, 1, 11), schedule_interval='@daily', catchup=False) as dag:
    args = {'start_date': dag.start_date, 'schedule_interval': dag.schedule_interval, 'catchup': dag.catchup}

    
    downloads = gd.taskgroup_download()

    check = BashOperator(
            task_id='check_files',
            bash_command='sleep 10'
        )
    process_a = BashOperator(
            task_id='process_a',
            bash_command='sleep 10'
        )

    process_b = BashOperator(
            task_id='process_b',
            bash_command='sleep 10'
        )
    
    process_c = BashOperator(
            task_id='process_c', 
            bash_command='sleep 10'
    )

downloads >> check >> [process_a, process_b, process_c]
