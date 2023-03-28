
#import modules
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from Twitter_ETL import run_etl_airflow


default_args = {
                'owner': 'airflow',
                'depends_on_past': False,
                'start_date': datetime(2023, 3, 22),
                'email': ['chanikya.d@hotmail.com'],
                'email_on_failure': True,
                'email_on_retry': True,
                'retries': 2,
                'retry_delay': timedelta(minutes = 1)
    }


dag = DAG(
          'twitter_dag',
          default_args = default_args,
          description='First ETL code'
    )


run_etl = PythonOperator(
                        task_id = 'complete_twitter_etl',
                        python_callable = run_etl_airflow,
                        dag = dag
    )

run_etl