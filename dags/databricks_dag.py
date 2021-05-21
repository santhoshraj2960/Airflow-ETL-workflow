"""
Databricks dag
"""
import airflow

from airflow import DAG
from airflow.contrib.operators.databricks_operator import DatabricksSubmitRunOperator

args = {
    'owner': 'pluralsightws165',
    'email': ['santhoshraj2960@hotmail.com'],
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(0)
}

dag = DAG(dag_id='example_databricks_operator', default_args=args, schedule_interval='@daily')

new_cluster = {
    'spark_version': '8.1.x-scala2.12',
    "node_type_id": "Standard_F4s",
    'num_workers': 1
}

notebook_task_params = {
    'new_cluster': new_cluster,
    'notebook_task': {
    'notebook_path': '/ETLProdNotebooks/facts/process_fact_yellow_taxi',
  },
}
# Example of using the JSON parameter to initialize the operator.
notebook_task = DatabricksSubmitRunOperator(
  task_id='notebook_task',
  dag=dag,
  json=notebook_task_params)
