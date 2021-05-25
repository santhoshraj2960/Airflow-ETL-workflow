"""
Databricks dag
"""
import os
import airflow
import requests
import json

from airflow import DAG
from airflow.contrib.operators.databricks_operator import DatabricksSubmitRunOperator, DatabricksRunNowOperator
from airflow.hooks.base_hook import BaseHook
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable

args = {
    'owner': 'pluralsightws165',
    'email': ['santhoshraj2960@hotmail.com'],
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(0)
}

dag = DAG(dag_id='ETL_newyork_taxi_operator', default_args=args, schedule_interval='@daily')
cluster_id = None


with dag:
    # Example of using the JSON parameter to initialize the operator.

    mount_storage_accounts = DatabricksRunNowOperator(
        task_id='mount_storage_accounts_task',
        job_id=100,
        notebook_params={}
    )

    copy_data_to_delta_lake = DatabricksRunNowOperator(
        task_id='copy_data_to_delta_lake_task',
        job_id=117,
        notebook_params={}
    )

    run_etl_yellow_taxi = DatabricksRunNowOperator(
        task_id='yellow_taxi_etl_task',
        job_id=108,
        notebook_params={}
    )

    run_etl_green_taxi = DatabricksRunNowOperator(
        task_id='green_taxi_etl_task',
        job_id=123,
        notebook_params={}
    )

    run_etl_fhv_taxi = DatabricksRunNowOperator(
        task_id='fhv_taxi_etl_task',
        job_id=133,
        notebook_params={}
    )

    un_mount_storage = DatabricksRunNowOperator(
        task_id='unmount_storage_after_etl_task',
        job_id=139,
        notebook_params={}
    )

    mount_storage_accounts >> copy_data_to_delta_lake
    copy_data_to_delta_lake >> [run_etl_yellow_taxi, run_etl_green_taxi, run_etl_fhv_taxi]
    [run_etl_yellow_taxi, run_etl_green_taxi, run_etl_fhv_taxi] >> un_mount_storage

# ------------------------ END OF FILE -------------------------------------------

'''
new_cluster = {
    'spark_version': '8.1.x-scala2.12',
    "node_type_id": "Standard_F4s",
    'num_workers': 0
}
'''

'''
def create_databricks_cluster(**kwargs):
    """

    :return: cluster_id
    """
    global cluster_id
    host = json.loads(BaseHook.get_connection("databricks_default").get_extra())['host']
    DOMAIN = host.split("https://")[1]
    TOKEN = json.loads(BaseHook.get_connection("databricks_default").get_extra())['token']

    response = requests.post(
        'https://%s/api/2.0/clusters/create' % DOMAIN,
        headers={'Authorization': 'Bearer %s' % TOKEN},
        json={
            "cluster_name": "my-cluster",
            "spark_version": "8.1.x-scala2.12",
            "node_type_id": "Standard_F4s",
            "spark_env_vars": {
                "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
            },
            "num_workers": 0,
            "autotermination_minutes": 30
        }
    )

    if response.status_code == 200:
        print(response.json()['cluster_id'])
        Variable.set('cluster_id', response.json()['cluster_id'])
    else:
        print("Error launching cluster: %s: %s" % (response.json()["error_code"], response.json()["message"]))
'''

'''
    notebook_task = DatabricksSubmitRunOperator(
        task_id='notebook_task',
        dag=dag,
        json={
            'existing_cluster_id': Variable.get('cluster_id'),
            'notebook_task': {
                'notebook_path': '/ETLProdNotebooks/setup_and_mount_storage',
            },
        })

    create_cluster_task = PythonOperator(
        task_id='create_cluster',
        python_callable=create_databricks_cluster,
    )
    '''
# print("********notebook task params = ", str(notebook_task_params))

'''
notebook_task2 = DatabricksRunNowOperator(task_id='notebook_task',
                                          dag=dag,
                                          json={
                                              'existing_cluster_id': Variable.get('cluster_id'),
                                              'notebook_task': {
                                                  'notebook_path': '/ETLProdNotebooks/setup_and_mount_storage',
                                              },
                                          })
'''
