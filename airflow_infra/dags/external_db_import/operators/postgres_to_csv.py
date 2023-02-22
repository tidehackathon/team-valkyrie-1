from airflow.models.baseoperator import BaseOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


class PostgresToCSVOperator(BaseOperator):
    def __init__(self, sql: str, filename: str, postgres_conn_id: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sql = sql
        self.filename = filename
        self.hook = PostgresHook(postgres_conn_id=postgres_conn_id)

    def execute(self, context):
        with open(self.filename, 'wt') as _:
            pass
        self.hook.copy_expert(sql=self.sql, filename=self.filename)
