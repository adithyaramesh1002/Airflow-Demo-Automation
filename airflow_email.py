from airflow import DAG
from airflow.operators import DummyOperator,EmailOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime.now() - timedelta(seconds=10),
    'retries': 0
}

dag = DAG('Sales_Nov', default_args=default_args, start_date=datetime.now() - timedelta(seconds=10))


op1 = DummyOperator(task_id='File1_landing', dag=dag)
t1 = EmailOperator(task_id='Processing_File_1',to='adithyaramesh1002@gmail.com',subject="Airflow_report",html_content="File 1 started",dag=dag)
op2 = DummyOperator(task_id='File2_landing', dag=dag)
t2 = EmailOperator(task_id='Processing_File_2',to='adithyaramesh1002@gmail.com',subject="Airflow_report",html_content="File 2 started",dag=dag)

op3 = DummyOperator(task_id='Aggregating', dag=dag)
op4 = DummyOperator(task_id='Final_Table_Push', dag=dag)



t1.set_upstream(op1)
t2.set_upstream(op2)
op3.set_upstream(t1)
op3.set_upstream(t2)  
op4.set_upstream(op3) 

