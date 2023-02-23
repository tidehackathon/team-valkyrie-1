# Valkyrie-1

# Tool description

**VIBI (Valkyrie Interoperability Business Intelligence)** - is a data analytics and visualization system for 
cross-nation testing events. The system architecture includes a data injection step from an external 
source, data cleansing and validation using Great Expectations, and data transformation using DBT 
open-source tool and Python. Transformed data is then stored in a Star schema architecture Data Warehouse. 
Data visualization and analysis are performed using two tools: PowerBI for data mining and discovery, 
and Metabase for business intelligence. The system also includes CI/CD, Orchestration, Monitoring, and 
Security tools. The BI Implementation approach follows a specific methodology, and there are KPIs used to 
measure the effectiveness of cross-nation testing, such as the Cross-Nation Interpretability Index, 
Multi-Domain Capability Coverage, and NDPP Capability Utilization Index. The system also proposes future 
improvements, including a Nation Page (Details) report, a Key Influencers report, a Test Standards Improvement 
Report, a Failed Test Cases Analysis Report, and a Nation Pairing Recommendation Report.

# High level architecture

The system architecture consists of several components that work together to process and analyze data from 
external sources, visualize it, and provide insights through various KPIs and reports.

At the core of the architecture is a data injection step that brings in data from an external database. The 
data is then cleansed and validated using the Great Expectations tool, and transformed using the DBT 
open-source tool and Python.

The transformed data is then moved to a data warehouse that is designed using a Star schema architecture, 
which is optimized for querying and performance. Two visualization tools, PowerBI and Metabase, are used 
for data mining, discovery, and business intelligence.

To manage the system, several other components are included, such as CI/CD, orchestration, monitoring, and 
security tools. Jenkins is used for CI/CD, Airflow for orchestration, Grafana for monitoring, and pgAdmin 
for security. The architecture is designed to support three different environments - DEV, TEST, and PROD.

The KPIs are used to measure the effectiveness of the testing process and provide insights on how different 
countries can work together. The three KPIs are the Cross-Nation Interpretability Index, Multi-Domain Capability 
Coverage, and the NDPP Capability Utilization Index. Reports, such as the Nation Page (Details), Key 
Influencers Report, Test Standards Improvement Report, Failed Test Cases Analysis Report, and Nation 
Pairing Recommendation Report, are also included to provide further insights and recommendations for improvement.

Overall, the architecture is designed to be flexible, scalable, and efficient, with the ability to handle 
large amounts of data and provide meaningful insights to improve testing processes.

# Used technologies and tools

- **Python** is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability 
with the use of significant indentation;
- **PostgreSQL** also known as Postgres, is a free and open-source relational database management system (RDBMS) 
emphasizing extensibility and SQL compliance. It was originally named POSTGRES, referring to its origins as 
a successor to the Ingres database developed at the University of California, Berkeley;
- **Data Analysis Expressions (DAX)** is the native formula and query language for Microsoft PowerPivot, Power BI 
Desktop and SQL Server Analysis Services (SSAS) Tabular models. DAX includes some of the functions that are 
used in Excel formulas with additional functions that are designed to work with relational data and perform 
dynamic aggregation. It is, in part, an evolution of the Multidimensional Expression (MDX) language developed 
by Microsoft for Analysis Services multidimensional models (often called cubes) combined with Excel formula 
functions. It is designed to be simple and easy to learn, while exposing the power and flexibility of PowerPivot 
and SSAS tabular models;
- **Great Expectations** is the leading tool for validating, documenting, and profiling your data to maintain 
quality and improve communication between teams. Head over to our getting started tutorial;
- **dbt** is an open-source command line tool that helps analysts and engineers transform data in their warehouse 
more effectively. It started at RJMetrics in 2016 as a solution to add basic transformation capabilities to 
Stitch (acquired by Talend in 2018). The earliest versions of dbt allowed analysts to contribute to the data 
transformation process following the best practices of software engineering;
- **Metabase** is an open-source business intelligence platform. You can use Metabase to ask questions about 
your data, or embed Metabase in your app to let your customers explore their data on their own;
- **Power BI** is an interactive data visualization software product developed by Microsoft with a primary 
focus on business intelligence. It is part of the Microsoft Power Platform. Power BI is a collection of 
software services, apps, and connectors that work together to turn unrelated sources of data into coherent, 
visually immersive, and interactive insights. Data may be input by reading directly from a database, webpage, 
or structured files such as spreadsheets, CSV, XML, and JSON;
- **ChatGPT (Chat Generative Pre-trained Transformer)** is a chatbot developed by OpenAI and launched in 
November 2022. It is built on top of OpenAI's GPT-3 family of large language models and has been fine-tuned 
(an approach to transfer learning) using both supervised and reinforcement learning techniques;
- **Apache Airflow** is an open-source workflow management platform for data engineering pipelines. It started 
at Airbnb in October 2014 as a solution to manage the company's increasingly complex workflows. Creating 
Airflow allowed Airbnb to programmatically author and schedule their workflows and monitor them via the 
built-in Airflow user interface. From the beginning, the project was made open source, becoming an 
Apache Incubator project in March 2016 and a top-level Apache Software Foundation project in January 2019;
- **Grafana** is a multi-platform open source analytics and interactive visualization web application. It provides 
charts, graphs, and alerts for the web when connected to supported data sources. There is also a licensed 
Grafana Enterprise version with additional capabilities available as a self-hosted installation or an account 
on the Grafana Labs cloud service. It is expandable through a plug-in system. End users can create 
complex monitoring dashboards using interactive query builders. Grafana is divided into a front end 
and back end, written in TypeScript and Go, respectively;
- **Jenkins** is a platform for creating a Continuous Integration/Continuous Delivery (CI/CD) environment. The 
system offers many tools, languages, and automation tasks to aid in pipeline creation when developing 
and deploying programs;
- **pgAdmin** is the most popular and feature rich Open Source administration and development platform for 
PostgreSQL, the most advanced Open Source database in the world. pgAdmin may be used on Linux, Unix, 
macOS and Windows to manage PostgreSQL and EDB Advanced Server 10 and above.

# DAY 4

## Updated Architecture overview

<img width="1174" alt="Screenshot 2023-02-23 at 12 13 09" src="https://user-images.githubusercontent.com/16081910/220900267-b47313ff-762e-4281-96a9-81f5d99f1b86.png">

## Updated BI Implementation Approach

<img width="1176" alt="Screenshot 2023-02-23 at 22 13 03" src="https://user-images.githubusercontent.com/16081910/221031777-8a08c0b3-9c42-405c-ae21-a1046fe4f525.png">

The project consists of such separate modules:

```
├── airflow_infra
├── documentation
├── executive_summary_generator
├── executive_summary_generator_api
├── external_data_import
├── metabase/dashboard/queries
├── powerbi
└── presentations
```

## documentation directory

A `documentation` directory with `TEAM_STORY.md` file which contains more deatails about team story.


## powerbi directory

A directory with PowerBI files.

## Setup & Run:

First you need to create and fill in the `.env` file in the `airflow_infra` directory:

```
AIRFLOW_IMAGE_NAME=apache/airflow:2.3.0
AIRFLOW_UID=50000

SRC_DATABASE_NAME=iodashboard
SRC_DATABASE_HOST=tidehackathon.postgres.database.azure.com
SRC_DATABASE_PORT=5432
SRC_DATABASE_USER=tidereader
SRC_DATABASE_PASS=ioH@ck@thonReader2023!

DST_DATABASE_NAME=postgres
DST_DATABASE_HOST=dst_db
DST_DATABASE_PORT=5432
DST_DATABASE_USER=postgres
DST_DATABASE_PASS=postgres
```

Also you need to create and fill another one `.env` file in `executive_summary_generator_api` as follows:

```
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```

```bash
cd airflow_infra
docker-compose --env-file .env up
```

___

# DAY 3

The project consists of such separate modules:

```
├── airflow_infra
├── executive_summary_generator
├── executive_summary_generator_api
├── external_data_import
├── metabase
├── national_pairing_recommendation
├── powerbi
└── presentations
```

## presentations directory

Contains PDF files with two presentations - one with general overview of all the work and the second one is architectural.

## national_pairing_recommendation module

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

```
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

### Updated general architecture
![MicrosoftTeams-image](https://user-images.githubusercontent.com/16081910/220406585-86534f8a-2fe4-4269-a4a7-c6c0220be03a.png)

The project consists of such separate modules:

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

```
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

```
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

```
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
