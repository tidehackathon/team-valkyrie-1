from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from cross_nation_interpretability_index.config import DST_DB_CONNECTION

with DAG(
        dag_id='fill_cross_nation_interpretability_index',
        start_date=datetime(2020, 1, 1),
        catchup=False,
) as dag:
    start_task = EmptyOperator(task_id='start_import')
    end_task = EmptyOperator(task_id='finish_import')

    create_table_task = PostgresOperator(
        task_id='create_table',
        sql='sql/create_cross_nation_interpretability_index_query.sql',
        postgres_conn_id=DST_DB_CONNECTION,
    )

    truncate_table_task = PostgresOperator(
        task_id='truncate_table',
        sql='sql/truncate_cross_nation_interpretability_index_query.sql',
        postgres_conn_id=DST_DB_CONNECTION,
    )

    insert_overall_task = PostgresOperator(
        task_id='insert_overall_scores',
        sql='sql/insert_overall_cross_nation_interpretability_index.sql',
        postgres_conn_id=DST_DB_CONNECTION,
    )

    insert_scores_by_domain_task = PostgresOperator(
        task_id='insert_scores_by_domain',
        sql='sql/insert_domain_cross_nation_interpretability_index.sql',
        postgres_conn_id=DST_DB_CONNECTION,
    )

    start_task >> create_table_task >> truncate_table_task >> insert_overall_task >> insert_scores_by_domain_task >> end_task
