from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.operators.dagrun_operator import TriggerDagRunOperator

dag = DAG(
    "dagrun1",
    description="r1",
    schedule_interval=None,
    start_date=datetime(2024, 5, 29),
    catchup=False,
)

task1 = BashOperator(task_id="task1", bash_command="sleep 5", dag=dag)
task2 = TriggerDagRunOperator(task_id="task2", trigger_dag_id="dagrun2", dag=dag)

task1 >> task2
