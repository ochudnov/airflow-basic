import os
import glob

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.subdag_operator import SubDagOperator
import dagfactory

AIRFLOW_DAGS = os.path.join(
    os.environ.get('AIRFLOW_HOME', os.getcwd()),
    'dags')

YAML_DAGS = os.path.join(AIRFLOW_DAGS, 'subdags', '*.yml')


def get_subdags(dag_name):
    subdags = dict()
    for dag_file in glob.glob(YAML_DAGS):
        dag_factory = dagfactory.DagFactory(dag_file)
        dag_factory.generate_dags(subdags)
    for subdag_name, subdag in subdags.items():
        subdag.dag_id = '{}.{}'.format(dag_name, subdag_name)
    return subdags


DAG_NAME = 'example_subdag_operator'

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id=DAG_NAME,
    default_args=args,
    schedule_interval='@once',
)

start = BashOperator(
    task_id='start',
    dag=dag,
    bash_command='echo "start"'
)

end = BashOperator(
    task_id='end',
    dag=dag,
    bash_command='echo "end"'
)


subdags = get_subdags(DAG_NAME)

if not subdags:
    start >> end


for subdag_name in subdags:
    op = SubDagOperator(
        task_id=subdag_name,
        subdag=subdags[subdag_name],
        dag=dag,
    )
    start >> op >> end
