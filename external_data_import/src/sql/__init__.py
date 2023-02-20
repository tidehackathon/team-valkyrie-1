import os
from pathlib import Path

BASE_DIR = Path(os.path.dirname(__file__))

with open(BASE_DIR / 'create_export_tables_query.sql', 'rt', encoding='utf-8') as query_file:
    CREATE_EXPORT_TABLES_QUERY = query_file.read()

with open(BASE_DIR / 'templated_count_query.sql', 'rt', encoding='utf-8') as query_file:
    TEMPLATED_COUNT_QUERY = query_file.read()

with open(BASE_DIR / 'templated_truncate_query.sql', 'rt', encoding='utf-8') as query_file:
    TEMPLATED_TRUNCATE_QUERY = query_file.read()

with open(BASE_DIR / 'templated_copy_all_to_stdout_query.sql', 'rt', encoding='utf-8') as query_file:
    TEMPLATED_COPY_ALL_TO_STDOUT_QUERY = query_file.read()
