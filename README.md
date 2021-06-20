# Airflow - ETL NYC taxi

Airflow is a workflow management tool developed by Apache. Airflow is used to model workflow of the ETL described below

The ETL pipeline used for this project is NYC yellow, green and fhv taxi trips data. 

Brief explanation of the ETL
1. The data is extracted in a raw format from Azure Data Lake gen 1 (**Bronze**) 
2. Transfromed to add KPIs (**Silver**) 
3. Facts and reports are created (**Gold**)
4. The reports are then stored it in a **delta lake** in **Azure Datalake Gen 2 storage**

[ETL code for respective taxi trips can be found here](https://github.com/santhoshraj2960/AzureDatabricksLearn/tree/main/notebooks/ETLProdNotebooks/)

**Postgres** is used to store the airflow's meta data (job runs and status)

Docker has also been used to facilitate easy setup

[Learning material used](https://app.pluralsight.com/library/courses/productionalizing-data-pipelines-apache-airflow/table-of-contents)


# ETL pipeline for generating facts of different NYC taxi

## Order of execution of tasks graph (DAG)
![alt text](https://github.com/santhoshraj2960/airflow_pluralsight/blob/main/screenshots/tasks_graph.png)

## Execution tree
![alt text](https://github.com/santhoshraj2960/airflow_pluralsight/blob/main/screenshots/tasks_tree.png)


## Databricks ETL jobs
![alt text](https://github.com/santhoshraj2960/airflow_pluralsight/blob/main/screenshots/azure_databricks_jobs.png)

## Master workflow scheduler

- [airflow dag](https://github.com/santhoshraj2960/airflow_pluralsight/blob/main/dags/databricks_dag.py)

## Databricks notebooks of ETL stages

- [Mount storage](https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/setup_and_mount_storage.ipynb)
 
- [Copy data to delta lake](https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/move_data_to_delta_lake.ipynb)
 
- [ETL Fhv taxi trips](https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/facts/process_fact_fhv_taxi.ipynb)
 
- [ETL Green taxi trips](https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/facts/process_fact_green_taxi.ipynb)
 
- [ETL Yellow taxi trips](https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/facts/process_fact_yellow_taxi.ipynb)
 
- [Unmount storage](https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/unmount_storage_and_cleanup.ipynb)


# Steps to run the project
1. Download docker
2. Clone the repo
3. Navigate to the main directory and run docker-compose up --build
4. Visit http://localhost:8080/ to view the dags
