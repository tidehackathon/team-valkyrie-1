# team-valkyrie-1

Valkyrie-1

# DAY 2

The project consists of three separate modules:

```
├── executive_summary_generator
├── external_data_import
└── metabase
```

Of which the following perform the corresponding functions:

+ **executive_summary_generator** - a module with the script that uses executive summary templates and OpaenAI API that helps create a short executive summary;
+ **external_data_import** - data injection module;
+ **metabase** - ....

## executive_summary_generator module

### Setup & run

First, you need to create OpenAI API Key on the https://platform.openai.com/ and write it down in a `.env` file.
An example of filled file is below:

```bash
OPENAI_API_KEY=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
```

Before run, you need to install dependencies in your Python virtual environment:

```bash
pip install -r executive_summary_generator/requirements.txt
```

And to run the module with example parameters use the following command:

```bash
python executive_summary_generator/run.py 
```

If you want to run the module with your input data, just edit the 
`example_input_data_for_summary` variable value in `run.py` file.

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

Before run, you need to install dependencies in your Python virtual environment:

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
## Architecture overview

### General architecture
![infrastructure-architecture](https://user-images.githubusercontent.com/16081910/220318950-c4c3e4d9-b02e-4353-8b3c-a0094b43bb65.png)

### Data warehouse model
![warehouse-architecture](https://user-images.githubusercontent.com/16081910/220319534-641a020d-2d54-4536-9b15-8ee6f6ed2c41.png)
