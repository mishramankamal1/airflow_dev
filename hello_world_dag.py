from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

#https://www.youtube.com/watch?v=IsWfoXY_Duk

def print_hello():
    return 'Hello world from first Airflow DAG!'

def print_hello2():
    return 'Hello world from second Airflow DAG!'

dag = DAG('hello_world', description='Hello World DAG',
          schedule_interval=None,
          start_date=datetime(2022, 3, 30), catchup=False)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)
hello_operator2 = PythonOperator(task_id='hello_task2', python_callable=print_hello2, dag=dag)



hello_operator >> hello_operator2
