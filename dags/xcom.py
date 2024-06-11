from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.operators.python_operator import PythonOperator

dag = DAG(
    "xcom",
    description="x",
    schedule_interval=None,
    start_date=datetime(2024, 5, 29),
    catchup=False,
)


def task_write(**kwarg):
    kwarg["ti"].xcom_push(key="valorxcom1", value=10200)


task1 = PythonOperator(task_id="task1", python_callable=task_write, dag=dag)


def task_read(**kwarg):
    valor = kwarg["ti"].xcom_pull(key="valorxcom1")
    print(f"O valor recuperado foi: {valor}")


task2 = PythonOperator(task_id="task2", python_callable=task_read, dag=dag)

task1 >> task2
