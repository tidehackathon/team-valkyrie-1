import logging
import time
from io import StringIO

import psycopg2

from .config import (
    DST_DATABASE_HOST,
    DST_DATABASE_NAME,
    DST_DATABASE_PASS,
    DST_DATABASE_PORT,
    DST_DATABASE_USER,
    TARGET_TABLES,
    SRC_DATABASE_HOST,
    SRC_DATABASE_NAME,
    SRC_DATABASE_PASS,
    SRC_DATABASE_PORT,
    SRC_DATABASE_USER,
)
from .sql import (
    CREATE_EXPORT_TABLES_QUERY,
    TEMPLATED_COPY_ALL_TO_STDOUT_QUERY,
    TEMPLATED_COUNT_QUERY,
    TEMPLATED_TRUNCATE_QUERY,
)

logger = logging.getLogger(__name__)


def main():
    src_conn = psycopg2.connect(
        database=SRC_DATABASE_NAME,
        host=SRC_DATABASE_HOST,
        port=SRC_DATABASE_PORT,
        user=SRC_DATABASE_USER,
        password=SRC_DATABASE_PASS,
    )
    src_conn.set_session(readonly=True)

    dst_conn = psycopg2.connect(
        database=DST_DATABASE_NAME,
        host=DST_DATABASE_HOST,
        port=DST_DATABASE_PORT,
        user=DST_DATABASE_USER,
        password=DST_DATABASE_PASS,
    )
    dst_conn.set_session(autocommit=True)

    try:
        with dst_conn, dst_conn.cursor() as cursor:
            cursor.execute(CREATE_EXPORT_TABLES_QUERY)

        for table in TARGET_TABLES:
            start = time.perf_counter()
            logger.info(f'Copying "{table}" table...')

            # The buffer will be used as an in-memory CSV file
            buffer = StringIO()

            with src_conn, src_conn.cursor() as cursor:
                cursor.copy_expert(sql=TEMPLATED_COPY_ALL_TO_STDOUT_QUERY.format(table=table), file=buffer)
            logger.debug('Data was successfully copied to the buffer')

            with dst_conn, dst_conn.cursor() as cursor:
                cursor.execute(TEMPLATED_TRUNCATE_QUERY.format(table=table))
            logger.debug('Destination table was successfully truncated')

            # Before starting reading, we need to move the pointer to the beginning of the file
            buffer.seek(0)

            with dst_conn, dst_conn.cursor() as cursor:
                cursor.copy_from(file=buffer, table=table, sep=',')
            logger.debug('Data was successfully copied from the buffer')

            with src_conn, src_conn.cursor() as cursor:
                cursor.execute(TEMPLATED_COUNT_QUERY.format(table=table))
                src_cnt, = cursor.fetchone()

            with dst_conn, dst_conn.cursor() as cursor:
                cursor.execute(TEMPLATED_COUNT_QUERY.format(table=table))
                dst_cnt, = cursor.fetchone()

            assert src_cnt == dst_cnt, f'Different count error: {src_cnt} in src vs {dst_conn} in dst'

            end = time.perf_counter()
            logger.info(f'Copying "{table}" table finished in {end - start:.04f} seconds')
    except psycopg2.DatabaseError as err:
        logger.error(f'Failed to import data, reason: {err}')
    finally:
        src_conn.close()
        dst_conn.close()
