# airflow-basic
The basic Apache Airflow setup (with `dag-factory`)

## Examples list
- `airflow/dags/create_tables_dag.yml` - utility DAG example
for creation tables. Has no schedule, should be triggered manually.
- `airflow/dags/create_user_dag.yml` - [XComs](https://airflow.apache.org/concepts.html#xcoms)
example. [Plugins](https://airflow.apache.org/plugins.html) example.
- `airflow/plugins/example_plugin.py` - an operator for retriving data from
SQLite DB.

## Installation
[Airflow official docs](https://airflow.apache.org/start.html)

[dag-factory PyPI page](https://pypi.org/project/dag-factory/)

Installation for OSX:
```
# set locales for python
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# install python3
brew install python3

# install virtualenv
pip3 install virtualenv

# create virtualenv
virtualenv -p python3 .venv

# activate virtualenv
source .venv/bin/activate

# setip deps
pip install -r requirements.txt

# set airflow home directory
export AIRFLOW_HOME=$(pwd)/airflow

# initialize the database
airflow initdb

# disable examples
sed -i '' -e 's/.*load_examples = True.*/load_examples = False/' airflow/airflow.cfg
airflow resetdb -y

# start the web server, default port is 8080
airflow webserver -p 8080 &

# start the scheduler
airflow scheduler

# visit localhost:8080 in the browser and enable the example dag in the home page

# kill the scheduler
# ctrl-c

# return the web from foreground
fg

# kill the web
# ctrl-c

# exit virtualenv
deactivate
```
