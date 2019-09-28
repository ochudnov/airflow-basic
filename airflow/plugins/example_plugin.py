from airflow.plugins_manager import AirflowPlugin

from airflow.hooks.sqlite_hook import SqliteHook
from airflow.operators.sqlite_operator import SqliteOperator


class GetResultSqliteOperator(SqliteOperator):
    def execute(self, context):
        self.log.info('Executing: %s', self.sql)
        hook = SqliteHook(sqlite_conn_id=self.sqlite_conn_id)
        return hook.get_records(self.sql, parameters=self.parameters)


class ExamplePlugin(AirflowPlugin):
    name = 'example_plugin'
    operators = [GetResultSqliteOperator]
