from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from external_db_import.config import (
    DAG_ID,
    DST_DB_CONNECTION,
    DST_DB_SCHEMA,
    IMPORT_TABLES,
    SRC_DB_CONNECTION,
)
from external_db_import.operators.csv_to_postgres import CSVToPostgresOperator
from external_db_import.operators.postgres_to_csv import PostgresToCSVOperator
from external_db_import.sql import (
    CREATE_EXPORT_TABLES_QUERY,
    TEMPLATED_COPY_ALL_TO_STDOUT_QUERY,
    TEMPLATED_TRUNCATE_QUERY,
)

with DAG(
        dag_id=DAG_ID,
        start_date=datetime(2020, 1, 1),
        catchup=False,
) as dag:
    start_task = EmptyOperator(task_id='start_import')
    end_task = EmptyOperator(task_id='finish_import')

    create_tables_task = PostgresOperator(
        task_id='create_tables',
        sql=CREATE_EXPORT_TABLES_QUERY.format(schema=DST_DB_SCHEMA),
        postgres_conn_id=DST_DB_CONNECTION,
    )

    start_task >> create_tables_task

    for table in IMPORT_TABLES:
        filename = f'{table}.csv'

        load_to_csv_task = PostgresToCSVOperator(
            task_id=f'load_to_csv_table__{table}',
            sql=TEMPLATED_COPY_ALL_TO_STDOUT_QUERY.format(table=table),
            filename=filename,
            postgres_conn_id=SRC_DB_CONNECTION,
        )

        truncate_target_table_task = PostgresOperator(
            task_id=f'truncate_table__{table}',
            sql=TEMPLATED_TRUNCATE_QUERY.format(table=f'{DST_DB_SCHEMA}.{table}'),
            postgres_conn_id=DST_DB_CONNECTION,
        )

        load_from_csv_task = CSVToPostgresOperator(
            task_id=f'load_from_csv_table__{table}',
            table=table,
            filename=filename,
            schema=DST_DB_SCHEMA,
            postgres_conn_id=DST_DB_CONNECTION,
            retries=2,
            retry_delay=timedelta(seconds=30),
        )

        create_tables_task >> load_to_csv_task >> truncate_target_table_task >> load_from_csv_task >> end_task
