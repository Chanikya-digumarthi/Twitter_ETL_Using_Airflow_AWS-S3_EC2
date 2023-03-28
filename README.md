<h1>Twitter_ETL_Using_Airflow_AWS-S3_EC2</h1>



<h2>Description</h2>
The goal of  this project is to extract tweets using Twitter API as JSON files. These jsons are then processed to be converted to table format. Then these tweeets are loaded into AWS S3 bucket. Here. Airflow is used for workflow orchestration which is run on AWS EC2 machine.
<br />

<h2>Prcess Flow</h2>
- <b>Twitter API ->  Uisng Twitter API, Tweets are scraped.<br />
- <b>Preprocessing ->  The tweets downloaded are in the form of JSON. For our case, we need them in the form of a table. so, this step is acheived using Python script. <br />
- <b>Write to AWS S3 -> The processed tweets are then stored as a CSV file in s3 bucket.<br />


<h2>Architecture</h2>
As shown in the diagram, Airflow runs on EC2 machine which is then connected to s3. The python scripts are used for defining Airflow DAG and ETL script for transformations. These scripts are attached to the repository. EC2 is accessed using terminal in the local machine.
The python script for DAG and ETL Operation are placed in EC2 instance and through Airfloww's web interface the DAG is run. It can also be scheduled to run at a specific schedule.

<h2>Languages and Tools used</h2>

- <b>Python 3.0<br />
- <b>Jupyter Notebooks<br />
- <b>Microsoft Visual Studio<br />
- <b>AWS EC2<br />
- <b>AWS S3<br />
- <b>Apache Airflow<br />
- <b>APIs<br />
