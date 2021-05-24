Repo that contains basic airflow tutorial. 

Airflow is used for scheduling and invoking tasks in an ETL pipeline

Postgres has been used to store the meta data of the tasks (or job) runs and job status

Docker has also been used to facilitate easy setup

Learning material used:
https://app.pluralsight.com/library/courses/productionalizing-data-pipelines-apache-airflow/table-of-contents


# ETL pipeline for generating facts of different NYC taxi

## Order of execution of tasks graph
![alt text](https://github.com/santhoshraj2960/airflow_pluralsight/blob/main/screenshots/tasks_graph.png)

## Execution tree
![alt text](https://github.com/santhoshraj2960/airflow_pluralsight/blob/main/screenshots/tasks_tree.png)


## Databricks ETL jobs
![alt text](https://github.com/santhoshraj2960/airflow_pluralsight/blob/main/screenshots/azure_databricks_jobs.png)


## Task Notebooks

- Mount storage: https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/setup_and_mount_storage.ipynb
- Copy data to delta lake: https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/move_data_to_delta_lake.ipynb
- ETL Fhv taxi trips: https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/facts/process_fact_fhv_taxi.ipynb
- ETL Green taxi trips: https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/facts/process_fact_green_taxi.ipynb
- ETL Yellow taxi trips: https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/facts/process_fact_yellow_taxi.ipynb
- Unmount storage: https://github.com/santhoshraj2960/AzureDatabricksLearn/blob/main/notebooks/ETLProdNotebooks/unmount_storage_and_cleanup.ipynb

