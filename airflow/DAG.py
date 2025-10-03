from asyncio import tasks
from datetime import datetime, timedelta
from pandas import * 


project_id = 'data-production-123'
POSTGRESS_CONNECTION_ID = 'dougs_db'

DATASET_NAME = "temp"


with DAG(
    'LoadCollab',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['data@dougs.fr'],
        'email_on_failure': False,
        'email_on_retry': False,
        'on_failure_callback': callback,
        'retries': 3,
        'retry_delay': timedelta(minutes=5),
    },
    description='Dougs ETL to extract data from csv to BigQuery',
    start_date= datetime(year=2022, month=7, day=28),
    schedule_interval=('0 22 * * *'),  # each night at 00:00 Paris TZ # NOT TRUE does he/she sees it
    catchup=False,
    tags=['ETL'],
) as dag:

    dataset = "collaborators.csv" 
    dataset2 = "ic_admins.csv" 
    dataset3 = "teams.csv" 
    dataset4 = "users.csv" 

    def load_collab(): 
        df = pd.read_csv(dataset)

    def load_table2(): 
        df = pd.read_csv(dataset2)

    def load_table3(): 
        df = pd.read_csv(dataset3)

    def load_table4(): 
        df = pd.read_csv(dataset4)

    def export_dataset(): 
        pd.to_csv('temp.csv')

    load_collab = PythonOperator(
        task_id='extract_load_collabs',
        python_callable=load_collab
    )

    load_users = PythonOperator(
        task_id='extract_load_users',
        python_callable=loadtable2()
    )

    load_ic_admins = PythonOperator(
        task_id='extract_load_ic_admins',
        python_callable=loadtable3()
    )

    load_teams = PythonOperator(
        task_id='extract_load_teams',
        python_callable=loadtable4()
    )

    export_dataset = PythonOperator(
        task_id='export_dataset',
        python_callable=export_dataset()
    )

    load_collab >> load_users >> load_ic_admins >> load_teams >> export_dataset
    