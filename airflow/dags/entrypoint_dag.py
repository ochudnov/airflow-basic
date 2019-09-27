import os
import glob
from airflow import DAG
import dagfactory

AIRFLOW_DAGS = os.path.join(
    os.environ.get('AIRFLOW_HOME', os.getcwd()),
    'dags')

YAML_DAGS = os.path.join(AIRFLOW_DAGS, '*.yml')

for dag_file in glob.glob(YAML_DAGS):
    dag_factory = dagfactory.DagFactory(dag_file)
    dag_factory.generate_dags(globals())
