# team-valkyrie-1

Valkyrie-1

# DAY 4

___

# DAY 3

The project consists of three separate modules:

```
├── airflow_infra
├── executive_summary_generator
├── executive_summary_generator_api
├── external_data_import
├── metabase
├── national_pairing_recommendation
└── presentations
```

## presentations

Contains PDF files with two presentations - one with general overview of all the work and the second one is architectural.

## national_pairing_recommendation

### Run

To start generating recommendations, run the following:

```bash
cd national_pairing_recommendation
python main.py
```

Additionally, `national_pairing_recommendation` directory has another `jupyter_notebooks` one. It consists of Jupyter Notebooks with calculations for national pairing recommendation algorithms, inculding input data.

## executive_summary_generator_api module

Rewritten the architecture for API and added one more endpoint that helps generating a short multidomain capability summary.

## airflow_infra module

### Setup & run

First, you need to create and fill in a `.env` file with parameters for connecting to two databases.
An example of filled file is below:

```bash
AIRFLOW_IMAGE_NAME=apache/airflow:2.3.0
AIRFLOW_UID=50000

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

Airflow is running in docker, so you need to run the following command to run:

```bash
docker-compose --env-file .env up
```
After that, you need to follow the link http://0.0.0.0:8080/ and login using `airflow` as login and password.

So far, one DAG has been implemented for importing data from an external database into an internal one:

![image_2023-02-22_15-14-15](https://user-images.githubusercontent.com/93226646/220654315-6082c2ea-4ddd-40d7-8d05-a627de671901.png)

## BI Implementation Approach

<img width="1180" alt="Screenshot 2023-02-22 at 16 04 45" src="https://user-images.githubusercontent.com/16081910/220662687-5e5bf068-892c-4f9c-ac83-ba78ae300802.png">

___

# DAY 2

## Architecture overview

### General architecture
![MicrosoftTeams-image](https://user-images.githubusercontent.com/16081910/220406585-86534f8a-2fe4-4269-a4a7-c6c0220be03a.png)

The project consists of three separate modules:

```
├── airflow_infra
├── executive_summary_generator
├── executive_summary_generator_api
├── external_data_import
└── metabase
```

Of which the following perform the corresponding functions:

+ **airflow_infra** - contains docker-compose for Airflow infrastructure deployment and DAGs that are going to be used in data pipelines; 
+ **executive_summary_generator** - a module with the script that uses executive summary templates and OpenAI API that helps create a short executive summary;
+ **executive_summary_generator_api** - a module that uses FastAPI framework and has an POST endpoint. The idea is to have API endpoint that takes some input text data, prepares executive summary templates and calls OpenAI API. As result it returns a short executive summary;
+ **external_data_import** - data injection module;
+ **metabase** - contains a list of files with Metabase queries that are going to be used as datasets for Metabase dashboards.

## executive_summary_generator module

### Setup & run

First, you need to create OpenAI API Key on the https://platform.openai.com/ and write it down in a `.env` file in the root of `executive_summary_generator` directory.

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


## executive_summary_generator_api module

### Setup & run

First, you need to create OpenAI API Key on the https://platform.openai.com/ and write it down in a `.env` file in the root of `executive_summary_generator_api` directory.

An example of filled file is below:

```bash
OPENAI_API_KEY=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
```

After creation of `.env` file, we recommend to run application using Docker. Use the following command to buid the image locally:

```bash
docker build . -t executive-summary-generator-api
```

And use this command to start thr docker container running:

```bash
docker run --rm --env-file .env -p 8000:8000 executive-summary-generator-api
```


## metabase module

At the moment, the board contains two implemented metrics, files with SQL code for which are located in the following directories:

```
dashboard
  └── queries
      ├── Cross-Nation Interpretability Index 2021.sql
      ├── Cross-Nation Interpretability Index 2022.sql
      ├── Cross-Nation Interpretability Index Diff.sql
      ├── Multi-Domain Capability Rate 2021.sql
      ├── Multi-Domain Capability Rate 2022.sql
      └── Multi-Domain Capability Rate Diff.sql
```

All these metrics are on the [board](http://metabase.valkyrie.org.ua/public/dashboard/47a3ce1b-752f-40ef-b40c-ba3fd6fc6fa7), a screenshot of the visualization is below:

![MicrosoftTeams-image (4)](https://user-images.githubusercontent.com/93226646/220414148-94fdb767-7c59-4170-8dd0-4ed1e6b7ba79.png)

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
We decided to convert the proposed database to a datawarehouse with a Star schema (see blow on the screenshot). It will give more flexibility and benefits for data management in the future.
![warehouse-architecture](https://user-images.githubusercontent.com/16081910/220319534-641a020d-2d54-4536-9b15-8ee6f6ed2c41.png)
