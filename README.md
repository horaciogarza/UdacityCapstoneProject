

## Scope the Project and Gather Data

### The goal of this project is to use the SARS-COV2 AKA COVID19 database for analytics purposes, using different technologies.

#### What you'll be able to do:
- Children that have passed away due to COVID-19
-   Dailycases
-   People that passed away having different comorbidities
-   Cases by state
-   Defunctions by men/women
- Correlations between different dimensions
 

#### Data Source: 
- datos.gob.mx (Mexican data-bank), 10 M 800K rows.
- datos.nl.gob.mx (Nuevo Leon, data-bank) 

#### Usage of data:
- Analytics
- DataScience

#### Data Cleansing/Harmonization

- Dates format we mixed (YYYY-MM-dd, MM-YYYY-dd )
- Column names coming from data dictionaries were change from 'CLAVES' to 'ID'
- Since the data is in spanish special characters were used.

#### Define the Data Model

- The model consist of one core table and catalogs.
	- CoreData (CoreTable)
	- Clasificacion (Catalog)
	- Municipios (Catalog)
	- Nacionalidad (Catalog)
	- Origen (Catalog)
	- ResultadoAntigeno (Catalog)
	- ResultadoLab (Catalog)
	- Sector (Catalog)
	- Sexo (Catalog)
	- SioNoCatalog (Catalog)
	- TipoDePaciente (Catalog)
	- Entidades (Catalog)

- Tables/Views for Analytics:
	- DailyReview, Dailycases
	- CasesByState, Cases by state
	- PercentageBasedOnGenre, Defunctions by men/women
 
Star Schema has been chosen due to the nature of the data, being the coredata table the center of it.
All of them include PRIMARY KEYs and coredata table include this keys as FOREIGN KEYS

####  ETL to Model the Data

-   ETL/ELT logic has been built using Python and Pandas, logic can be found on playground.py file
- paths.py file define the path of all the CSV files
- sql_queries.py define all the queries in case of needed
- executed_queries.sql defines all the SQL queries in order to set-up the database.
- Data is included in the data folder (Core data can't be included since it's too heavy, but the download link can be found here https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico)

#### Write Up

**- Technologies used:**
- PostgreSQL: Used as a relational database, I've decided to use it cause for this purposes a NoSQL database wont fit at 100% since the growing is vertical and not horizontal.
- Pandas: Pandas has been chosen as the technology that is managing the data and reading CSV files
- Transformation has been done in the database as stored procedures and the python file will execute them.
	- Why? Because in the future it's easier to mantain a SQL Stored Procedure than code.
-   Mexican Data Bank.



## Include a description of how you would approach the problem differently under the following scenarios:
   -   If the data was increased by 100x.
	   - The same way with the difference that I'll include a non-clustered index on the table, deactivating when we upload data and enable it again when data is complete.
	   - Using Apache Spark and PySpark to deal with a really large amount of data
   -   If the pipelines were run on a daily basis by 7am.
	   - Airflow can suit here as well since we can schedule tasks and see it on a graphical way and cofigure it to send notification emails.
   -   If the database needed to be accessed by 100+ people.
	   - Migrate to AWS, to prevent a potential risk to all the users when loading new data.

#### RESULTS

![enter image description here](https://i.imgur.com/y6pWTWX.jpg)



## FAQ

- Why don't you upload all catalog data using the ETL tool?
	- According to the databank, catalogs haven't change since the creation of them