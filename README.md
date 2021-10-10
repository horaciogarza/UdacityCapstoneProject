
## Scope the Project and Gather Data

### The goal of this project is to use the covidf19 database for analytics purposes, using different technologies.

#### Data Source: 
- datos.gob.mx (Mexican data-bank)
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
	- Children that have passed away due to COVID-19
	- Dailycases
	- People that passed away having different comorbidities
	- Cases by state
	- Defunctions by men/women
 
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
   -   If the pipelines were run on a daily basis by 7am.
	   - This is prepared to work on a daily basis, I'll include an email notification.
   -   If the database needed to be accessed by 100+ people.
	   - Manage permissions GRANT permission when data is there and REVOKE permission to tables if the data is still loading in order to avoid BLOCKING TABLES.

## FAQ

- Why don't you upload all catalog data using the ETL tool?
	- According to the databank, catalogs haven't change since the creation of them