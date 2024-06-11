# Domine Apache Airflow. https://www.eia.ai/
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import statistics as sts

dag = DAG(
    "pythonop",
    description="pythonop",
    schedule_interval=None,
    start_date=datetime(2023, 3, 5),
    catchup=False,
)


def data_cleaner():
    df = pd.read_csv("/opt/airflow/data/Churn.csv", sep=";")
    df.columns = [
        "id",
        "score",
        "estado",
        "genero",
        "idade",
        "patrimonio",
        "saldo",
        "produtos",
        "temCartCredito",
        "ativo",
        "salario",
        "saiu",
    ]
    mediana = sts.median(df["salario"])
    df["salario"].fillna(mediana, inplace=True)
    df["genero"].fillna("Masculino", inplace=True)
    mediana = sts.media(df["idade"])
    df.loc[(df["idade"] < 0) | (df["idade"] > 120)] = mediana
    df.drop_duplicates(subset="id", keep="first", inplace=True)
    df.to_csv("/opt/airflow/data/Churn2.csv", sep=";", index=False)


t1 = PythonOperator(task_id="t1", python_callable=data_cleaner, dag=dag)

t1
