from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.operators.dagrun_operator import TriggerDagRunOperator

dag = DAG(
    "dagrun2",
    description="r2",
    schedule_interval=None,
    start_date=datetime(2024, 5, 29),
    catchup=False,
)

task1 = BashOperator(task_id="task1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="task2", bash_command="sleep 5", dag=dag)

task1 >> task2
