# The team story of  Valkyrie 1

## Intro

The Valkyrie is an ancient symbol that represents the protection of Wisdom, Justice, Nobility, and Honor. It 
is particularly significant among warriors who defend their homeland, ancestral heritage, and beliefs. As 
a protective symbol, it was used by priests to preserve the ancient ways.

We are a group of IT volunteers who came together in response to the aggressive russian invasion of 
Ukraine. Our mission is to create software tools that will help the Ukrainian army defend our land more 
effectively. We are passionate about using our skills to make a positive impact in our country and 
will continue to work tirelessly to achieve our goals.

We decided to call our tool as **VIBI**. It stands for **Valkyrie Interoperability Business Intelligence**.

## Architecture overview

The fist and main thing we started working on is the architecture for our system.
<img width="1174" alt="Screenshot 2023-02-23 at 12 13 09" src="https://user-images.githubusercontent.com/16081910/220890731-91b828fe-f534-40cc-bdae-4cf512190d51.png">

**_NOTE:_**  Pay attention that there are background color differences in diagram components.
The components with white background color are the ones that are already implemented. The grey background color
means that it future components that will be implemented.

### System flow

- The starting point in our system is data injection step, which takes data from external sources. In our case,
it is external `iodashboard` DB. It is a manual operation like run the Python script which takes data from one
source to another in the most effective way;
- Next step is to perform the cleansing and validation for our fresh data using Great expectations tool;
- To make necessary data transformations easily, we are going to use DBT open-source tool together with Python;
- After DBT usage all transformed data are moving to the Data Warehouse. It has Star schema architecture (see below);
- The next step is, probably, the main one - data visualisation and analysis. Here we are using two visualisation tools:
PowerBI and Metabase. The first one is a Desktop version, which is free if you run it locally on your machine. 
Additionally, it can be shared in your own workspace for free. In our system it is used for data mining and 
data discovery. Speaking about Metabase, we are using the community version which is completely free. It is used to
show interactive dashboards and visualisations, in other words - business intelligence. 
- Behind the scenes, we are also, having a CI/CB, Orchestration, Monitoring and Security stuff. For CI/CB it will be
a Jenkins, for Orchestration - Airflow, for Monitoring - Grafana and, for security reasons, we are going to 
use pgAdmin to avoid direct connections to all our DBs;
- To follow the best practises, we are going to have 3 type of environments - DEV, TEST and PROD.

## Data Warehouse overview
<img width="1175" alt="Screenshot 2023-02-23 at 12 14 03" src="https://user-images.githubusercontent.com/16081910/220890893-331d6901-cbc9-4485-bbf8-597c165e6899.png">

We were given a DB with input data at the beginning of TIDE Hackathon. Our team has found that the provided DB has 
schema which can be optimized - some tables had mixed entities. That's why we are using Star schema in our
Data Warehouse. It will give us a boost in querying, aggregation and performance.

## BI Implementation Approach

We had started adapting to conditions we are in to reach the success. We have found the approach which will 
lead us to it. You can see it on the picture below:
<img width="745" alt="image" src="https://user-images.githubusercontent.com/16081910/221043808-8098967d-50a7-46b9-9cd3-43f726a7103f.png">

## KPIs

### Cross-Nation Interopretability Index

The Cross-Nation Interopretability Index is a way to measure how well countries can work together when they do tests. 
It looks at how good the results are when one country makes the tests, and another country uses them. This can help 
us determine how to improve testing and make it easier for countries to work together.
<img width="994" alt="image" src="https://user-images.githubusercontent.com/16081910/221034286-e9e67ea0-8030-49bc-a019-6bd3148f56c4.png">


### Multi-Domain Capability Coverage

Capability Multi-Domain Coverage is a metric that shows the percentage of testing in which capabilities are used 
in multiple operational domains. It helps to assess the ability of different countries to work together in diverse 
situations and identify areas for improvement.
<img width="757" alt="Screenshot 2023-02-23 at 22 20 13" src="https://user-images.githubusercontent.com/16081910/221032926-72eb8bb7-6b7c-4b73-a54e-cf78e19bdee2.png">


### NDPP Capability Utilization Index

The NDPP Capability Utilization Index measures how effectively nations use NATO-recommended capabilities during 
CWIX events, identifying areas for improvement and maximizing available resources.
<img width="754" alt="image" src="https://user-images.githubusercontent.com/16081910/221033016-52e2c1ef-7617-46d4-9566-97a4dce450cb.png">


## Proposals for Future CWIX Events improvements

### Nation Page (Details)

The report provides a visual overview of each nation's capabilities, test cases, and test partners in CWIX events. 
This allows for easy analysis and decision-making on the overall success of participation in CWIX, 
viewable per-nation basis.

### Key Influencers Report

The Key Influencers report provides insights on the Cross-Nation Intero
pretability Index, Multi-Domain Capability 
Coverage, and NDPP Capability Utilization Index, helping identify areas for improvement.
<img width="636" alt="Screenshot 2023-02-23 at 12 17 14" src="https://user-images.githubusercontent.com/16081910/220891450-5a70ac82-770a-4ec4-844f-3b2bba09e70e.png">

### Test Standards Improvement Report

The Test Standards Improvement Report identifies which standards caused issues during testing and need improvement. 
It helps to ensure that tests are more effective and efficient, leading to better overall results.

<img width="1162" alt="image" src="https://user-images.githubusercontent.com/16081910/221044249-94542002-6434-4b3e-86c6-af2c02d95318.png">


### Failed Test Cases Analysis Report

The Failed Test Cases Analysis Report evaluates test cases that have consistently failed over time, identifying 
which cases should be reconsidered or recreated to improve overall testing effectiveness.

<img width="1163" alt="image" src="https://user-images.githubusercontent.com/16081910/221043963-afe7facb-1999-44d1-9198-0acd7dc736e2.png">

### Nation Pairing Recommendation Report

The Nation Pairing Recommendation Report suggests which countries should conduct testing together for better 
coverage and efficiency while avoiding repeated testing.

<img width="1162" alt="image" src="https://user-images.githubusercontent.com/16081910/221044412-bc1216a5-9dea-4381-b775-511e5f4b75d9.png">

