import os

from airflow import settings
from airflow.models import Connection

session = settings.Session()

DAG_ID = 'external_db_import_v2'

# External database
SRC_DB_CONNECTION = 'src_postgres_db'
SRC_DB_SCHEMA = 'public'

conn = Connection(
    conn_type='Postgres',
    conn_id=SRC_DB_CONNECTION,
    host=os.getenv('SRC_DATABASE_HOST'),
    login=os.getenv('SRC_DATABASE_USER'),
    password=os.getenv('SRC_DATABASE_PASS'),
    port=os.getenv('SRC_DATABASE_PORT'),
    schema=os.getenv('SRC_DATABASE_NAME'),
)

if not session.query(Connection).filter_by(conn_id=SRC_DB_CONNECTION).first():
    session.add(conn)
    session.commit()

# Stage database
DST_DB_CONNECTION = 'dst_postgres_db'
DST_DB_SCHEMA = 'staging'

conn = Connection(
    conn_type='Postgres',
    conn_id=DST_DB_CONNECTION,
    host=os.getenv('DST_DATABASE_HOST'),
    login=os.getenv('DST_DATABASE_USER'),
    password=os.getenv('DST_DATABASE_PASS'),
    port=os.getenv('DST_DATABASE_PORT'),
    schema=os.getenv('DST_DATABASE_NAME'),
)

if not session.query(Connection).filter_by(conn_id=DST_DB_CONNECTION).first():
    session.add(conn)
    session.commit()

IMPORT_TABLES = (
    'ndpp_capabilities',
    'warfare_levels',
    'capability_operational_domains',
    'capability_tasks',
    'capability_warfarelevels',
    'focus_areas',
    'objectives',
    'nations',
    'capabilities',
    'operational_domains',
    'standards',
    'tasks',
    'testcases',
    'test_objectives',
    'test_participants',
    'issue_categories',
    'testcase_issue_categories',
    'testcase_standards',
)
