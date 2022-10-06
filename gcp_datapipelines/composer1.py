#step1:- import libraries
#step2:- dag default arguments
#step3:- build tasks with opearators
#step4:- order tasks sequential
###############################
import datetime
import requests
from airflow import models
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator 
from airflow.operators.empty import EmptyOperator 
from airflow.models import Variable
# from airflow.providers.google import dataflow

# from airflow import D
default_dag_args = {
    # The start_date describes when a DAG is valid / can be run. Set this to a
    # fixed point in time rather than dynamically, since it is evaluated every
    # time a DAG is parsed. See:
    # https://airflow.apache.org/faq.html#what-s-the-deal-with-start-date
    'start_date': datetime.datetime(2022, 10, 1),
    'depends_on_past': False
}

# Define a DAG (directed acyclic graph) of tasks.
# Any task you create within the context manager is automatically added to the
# DAG object.
with models.DAG(
    'dagcheck_1',
    default_args=default_dag_args,
    schedule_interval='@once') as dag:
    def check(num):
        if num%2==0:
            return "even"
        else:
            return "odd"
    # pytask=PythonOperator(
    #     task_id="pytester",
    #     python_callable=check(827346)
    # )


    # bashtask=BashOperator(
    #     task_id="btask",
    #     bash_command="echo $1"
    # )

    # btask2=BashOpearator(
    #     task_id="urlcheck",
    #     bash_command="gsutil "
    # )

#     templated_command = """
#     {% for i in range(1) %}
#         echo "###########################"
#         ping "{{ params.url }}"
#     {% endfor %}
# """

    start=EmptyOperator(
        task_id="start_task"
    )
    # t3 = BashOperator(
    #     task_id='templated',
    #     bash_command="echo '########';sudo ping google.com"
    #     # params={'url': 'https://google.com'}
    #     )



    def url_checker(url,**context):
        print(context)
        try:
            #Get Url
            get = requests.get(url)
            # if the request succeeds 
            if get.status_code == 200:
                return(f"{url}: is reachable")
            else:
                return(f"{url}: is Not reachable, status_code: {get.status_code}")

        #Exception
        except requests.exceptions.RequestException as e:
            # print URL with Errs
            raise SystemExit(f"{url}: is Not reachable \nErr: {e}")
            #exit(1) ## to fail task

    pycheck=PythonOperator(
        task_id='url_Check',
        python_callable=url_checker,
        op_args=Variable.get('dagcheck_1_var',deserialize_json=True)
    )

    end=EmptyOperator(
        task_id="end_task"
    )
    start >> pycheck >> end