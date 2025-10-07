from asyncio import tasks
from datetime import datetime, timedelta
from pandas import * 
from airflow import DAG
from airflow.operators.python import *

project_id = 'data-production-123'




def export_to_bq(dataset_name, table_name):
    print("file sent to BQ :)")

    

dataset_name = 'bronze_monolith_global'


with DAG(
    'LoadCollab',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['data@dougs.fr'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=5),
    },
    description='Dougs ETL to extract data from csv to BigQuery',
    start_date= datetime(year=2022, month=7, day=28),
    schedule_interval=('0 22 * * *'),  # each night at 00:00 Paris TZ
    catchup=False,
    tags=['ETL'],
) as dag:

    dataset = "collaborators.csv" 
    dataset2 = "ic_admins.csv" 
    dataset3 = "teams.csv" 
    dataset4 = "users.csv" 

    def load_collab(): 
        df = read_csv(dataset)
        return df

    def load_table2(): 
        df = read_csv(dataset2)
        return df

    def load_table3(): 
        df = read_csv(dataset3)
        return df

    def load_table4(): 
        df = read_csv(dataset4)
        return df

    def export_dataset(ti, task_id, **context):
        # Pull the DataFrame directly from the upstream task's XCom
        df = ti.xcom_pull(task_ids=task_id)
        export_to_bq(dataset_name , table_name)


    load_collab = PythonOperator(
        task_id='extract_load_collabs',
        python_callable=load_collab
    )

    load_users = PythonOperator(
        task_id='extract_load_users',
        python_callable=load_table2
    )

    load_ic_admins = PythonOperator(
        task_id='extract_load_ic_admins',
        python_callable=load_table3
    )

    load_teams = PythonOperator(
        task_id='extract_load_teams',
        python_callable=load_table4
    )

    export_dataset_collab = PythonOperator(
        task_id='export_dataset_1',
        python_callable=export_dataset,
        op_kwargs = {'task_id':'extract_load_collabs'}
    )

    export_dataset_users = PythonOperator(
        task_id='export_dataset_2',
        python_callable=export_dataset,
        op_kwargs = {'task_id':'extract_load_users'}
    )

    export_dataset_ic_admins = PythonOperator(
        task_id='export_dataset_3',
        python_callable=export_dataset,
        op_kwargs = {'task_id':'extract_load_ic_admins'}
    )

    export_dataset_teams = PythonOperator(
        task_id='export_dataset_4',
        python_callable=export_dataset,
        op_kwargs = {'task_id':'extract_load_teams'}
    )

    load_collab >> load_users >> load_ic_admins >> load_teams >> [export_dataset_collab,export_dataset_users,export_dataset_ic_admins,export_dataset_teams]
    