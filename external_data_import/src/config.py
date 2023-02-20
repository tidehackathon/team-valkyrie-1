from environs import Env

env = Env()
env.read_env()

# External database
SRC_DATABASE_NAME = env('SRC_DATABASE_NAME')
SRC_DATABASE_HOST = env('SRC_DATABASE_HOST')
SRC_DATABASE_PORT = env('SRC_DATABASE_PORT')
SRC_DATABASE_USER = env('SRC_DATABASE_USER')
SRC_DATABASE_PASS = env('SRC_DATABASE_PASS')

# Stage database
DST_DATABASE_NAME = env('DST_DATABASE_NAME')
DST_DATABASE_HOST = env('DST_DATABASE_HOST')
DST_DATABASE_PORT = env('DST_DATABASE_PORT')
DST_DATABASE_USER = env('DST_DATABASE_USER')
DST_DATABASE_PASS = env('DST_DATABASE_PASS')

TARGET_TABLES = (
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
