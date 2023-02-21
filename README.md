# team-valkyrie-1

Valkyrie-1

# DAY 2

___

# DAY 1

## High-level project structure


The project consists of three separate modules:

```
├── executive_summary_generator_api
├── external_data_import
└── metabase
```

Of which the following perform the corresponding functions:

+ **executive_summary_generator_api** - ...;
+ **external_data_import** - data injection module;
+ **metabase** - ....

## external_data_import module

### Setup & run

First, you need to create and fill in a `.env` file with parameters for connecting to two databases.
An example of filled file is below:

```bash
SRC_DATABASE_NAME=src_db
SRC_DATABASE_HOST=192.168.0.1
SRC_DATABASE_PORT=5432
SRC_DATABASE_USER=some_user
SRC_DATABASE_PASS=just_password

DST_DATABASE_NAME=dst_db
DST_DATABASE_HOST=192.168.0.1
DST_DATABASE_PORT=5432
DST_DATABASE_USER=other_user
DST_DATABASE_PASS=secret_password
```

Before run, you need to install dependencies:

```bash
pip install -r external_data_import/requirements.txt
```

And to run import use the following command:

```bash
python external_data_import/run.py 
```

## executive_summary_generator_api module

...

## metabase module

...
