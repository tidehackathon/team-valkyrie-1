from copy import deepcopy

import psycopg2
import psycopg2.extensions
import psycopg2.extras
from airflow.providers.postgres.hooks.postgres import PostgresHook
from psycopg2.extensions import connection


class PostgresSchemaHook(PostgresHook):
    def __init__(self, db_schema: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_schema = db_schema

    def get_conn(self) -> connection:
        conn_id = getattr(self, self.conn_name_attr)
        conn = deepcopy(self.connection or self.get_connection(conn_id))

        if conn.extra_dejson.get("iam", False):
            conn.login, conn.password, conn.port = self.get_iam_token(conn)

        conn_args = dict(
            host=conn.host,
            user=conn.login,
            password=conn.password,
            dbname=conn.schema,
            port=conn.port,
            options=f'-c search_path={self.db_schema}'
        )
        raw_cursor = conn.extra_dejson.get("cursor", False)
        if raw_cursor:
            conn_args["cursor_factory"] = self._get_cursor(raw_cursor)

        for arg_name, arg_val in conn.extra_dejson.items():
            if arg_name not in [
                "iam",
                "redshift",
                "cursor",
                "cluster-identifier",
                "aws_conn_id",
            ]:
                conn_args[arg_name] = arg_val

        self.conn = psycopg2.connect(**conn_args)
        return self.conn
