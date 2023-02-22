from airflow.models.baseoperator import BaseOperator

from external_db_import.operators.postgres_schema_hook import PostgresSchemaHook


class CSVToPostgresOperator(BaseOperator):
    def __init__(self, filename: str, table: str, schema: str, postgres_conn_id: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = filename
        self.table = table
        self.hook = PostgresSchemaHook(
            db_schema=schema,
            postgres_conn_id=postgres_conn_id,
        )

    def execute(self, context):
        conn = self.hook.get_conn()
        with conn, conn.cursor() as cursor, open(self.filename, 'rt') as file:
            cursor.copy_from(file=file, table=self.table, sep=',')
