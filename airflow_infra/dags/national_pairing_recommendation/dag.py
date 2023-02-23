from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from national_pairing_recommendation.config import DST_DB_CONNECTION, DST_DB_SCHEMA
from national_pairing_recommendation.operators.csv_to_postgres import CSVToPostgresOperator
from national_pairing_recommendation.operators.postgres_to_csv import PostgresToCSVOperator
from national_pairing_recommendation.predict_scores import predict

with DAG(
        dag_id='create_national_pairing_recommendation',
        start_date=datetime(2020, 1, 1),
        catchup=False,
) as dag:
    start_task = EmptyOperator(task_id='start_import')
    end_task = EmptyOperator(task_id='finish_import')

    create_table_task = PostgresOperator(
        task_id='create_table',
        sql='sql/create_national_pairing_recommendation.sql',
        postgres_conn_id=DST_DB_CONNECTION,
    )

    truncate_table_task = PostgresOperator(
        task_id='truncate_table',
        sql='sql/truncate_national_pairing_recommendation.sql',
        postgres_conn_id=DST_DB_CONNECTION,
    )

    for operational_domain_id in ('NULL', 1, 2, 3, 4, 5, 6):
        load_data_task = PostgresToCSVOperator(
            task_id=f'load_domain__{operational_domain_id}',
            sql='COPY (SELECT consumer_id, provider_id, score FROM cross_nation_interpretability_index WHERE operational_domain_id {}) TO STDOUT WITH DELIMITER \',\''.format(
                f'= {operational_domain_id}' if operational_domain_id != 'NULL' else 'IS NULL'
            ),
            filename=f'{operational_domain_id}.csv',
            postgres_conn_id=DST_DB_CONNECTION,
        )

        create_prediction_task = PythonOperator(
            task_id=f'create_prediction_domain__{operational_domain_id}',
            python_callable=predict,
            op_kwargs={'operational_domain_id': operational_domain_id},
        )

        load_prediction_task = CSVToPostgresOperator(
            filename=f'{operational_domain_id}.csv',
            table='national_pairing_recommendation',
            task_id=f'load_prediction_domain__{operational_domain_id}',
            schema=DST_DB_SCHEMA,
            postgres_conn_id=DST_DB_CONNECTION,
        )

        start_task >> load_data_task >> create_prediction_task >> create_table_task >> truncate_table_task >> load_prediction_task >> end_task
