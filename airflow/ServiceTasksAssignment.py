from asyncio import tasks
from datetime import datetime, timedelta
from utils.global_validation_operator import *
from utils.bigquery_operator import *
from utils.slack_operator import * 
from service_tasks_assignment import * 
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow import DAG


project_id = 'data-production-398108'
POSTGRESS_CONNECTION_ID = 'dougs_postgres_replica'

DATASET_PREFIX = ''
DATASET_NAME = "bronze_service_tasks_assignment"
callback = task_fail_slack_alert

if Variable.get("env") == 'dev':
    DATASET_PREFIX += 'dev_'
    callback = None


with DAG(
    'ServiceTasksAssignment',
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
    description='Dougs ETL to extract data from prod to BigQuery',
    start_date= datetime(year=2022, month=7, day=28),
    schedule_interval=('0 22 * * *'),  # each night at 00:00 Paris TZ
    catchup=False,
    tags=['ETL'],
) as dag:


    dataset = DATASET_PREFIX + DATASET_NAME


    load_collaborators = PythonOperator(
        task_id='extract_load_collaborators',
        python_callable=postgresToBigquery,
        op_kwargs={'project_id': project_id, 'dataset': dataset, 'tablename': 'collaborators',
                'sql_query':getCollaboratorsSql(), 'schema':getCollaboratorsSchema(), 'postgres_conn':POSTGRESS_CONNECTION_ID}
    )
         
    load_teams = PythonOperator(
        task_id='extract_load_teams',
        python_callable=postgresToBigquery,
        op_kwargs={'project_id': project_id, 'dataset': dataset, 'tablename': 'teams',
                'sql_query':getTeamsSql(), 'schema':getTeamSchema(), 'postgres_conn':POSTGRESS_CONNECTION_ID}
    )
    

    create_task_assignment_dataset = createDatasetIfNotExist(project_id, dataset)
    create_task_assignment_dataset >> [
        load_collaborators,
        load_teams]
    
     