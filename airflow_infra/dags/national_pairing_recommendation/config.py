import os

from airflow import settings
from airflow.models import Connection

session = settings.Session()

# Stage database
DST_DB_CONNECTION = 'dst_postgres_db'
DST_DB_SCHEMA = 'public'

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
