# airflow-basic
The basic Apache Airflow setup (with `dag-factory`)

## Airflow quick install
[Airflow official docs](https://airflow.apache.org/start.html)

[dag-factory PyPI page](https://pypi.org/project/dag-factory/)

Step by step (OSX):
```
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
sed -i sed 's/.*load_examples = True.*/load_examples = False/' airflow/airflow.cfg
rm -f airflow/airflow.cfgsed
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
