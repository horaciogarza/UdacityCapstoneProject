import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
from paths import *
from datetime import datetime


def main():
    """
        Main Function:

        This function connects to the database, it creates a cursos and executes the coredatafile and data cleansing process.

    """
    print("Establishing connection")
    conn = psycopg2.connect("host=localhost dbname=UdacityCapstoneProject user=postgres password=6886780")
    cur = conn.cursor()
    filepath = "data/coredata.csv"
    print("Connection complete")

    #Revoking access to avoid table block from users
    cur.execute(sp_revoke_access)

    process_coredata_file(cur, filepath, conn)
    process_data_cleansing(cur)

    #Granting access again
    cur.execute(sp_grant_access)




    conn.commit()



def process_coredata_file(cur, filepath, conn):
    """
        process_coredata_file Function:
        PARAMETERS:
            cur: Cursor object
            filepath: The path of the CSV file

        This function connects to the database and inserts all the rows that the CSV contains """
    
    print("Reading file", filepath)
    df = pd.read_csv(filepath, parse_dates=['FECHA_ACTUALIZACION','FECHA_INGRESO','FECHA_SINTOMAS','FECHA_DEF'])
    print("Reading complete")

    df['ID_REGISTRO'] = df['ID_REGISTRO'].astype(str)
    df['FECHA_DEF'] = df['FECHA_DEF'].astype(str)
    df['PAIS_NACIONALIDAD'] = df['PAIS_NACIONALIDAD'].astype(str)
    df['PAIS_ORIGEN'] = df['PAIS_ORIGEN'].astype(str)

    

    

    #getting the count before inserting values for unit test purposes
    cur.execute(count_of_coretable)
    result = cur.fetchone()
    countBeforeInserting = result[0]

    #Deleting before inserting
    cur.execute(coredata_table_delete)
    

    print("Uploading data")

    totalRows = len(df.index)
    totalRowsInserted = 0
    countAfterInserting = 0
    countBeforeInserting = 0

   

    df2 = df.iloc[:20]

    for index, row in df2.iterrows():
        print("Inserting row ",index+1)

        data_to_upload = [row.FECHA_ACTUALIZACION, row.ID_REGISTRO,   row.ORIGEN,    row.SECTOR,    row.ENTIDAD_UM,    row.SEXO,  row.ENTIDAD_NAC,   row.ENTIDAD_RES,   row.MUNICIPIO_RES, row.TIPO_PACIENTE, row.FECHA_INGRESO, row.FECHA_SINTOMAS,    row.FECHA_DEF, row.INTUBADO,  row.NEUMONIA,  row.EDAD,  row.NACIONALIDAD,  row.EMBARAZO,  row.HABLA_LENGUA_INDIG,    row.INDIGENA,  row.DIABETES,  row.EPOC,  row.ASMA,  row.INMUSUPR,  row.HIPERTENSION,  row.OTRA_COM,  row.CARDIOVASCULAR,    row.OBESIDAD,  row.RENAL_CRONICA, row.TABAQUISMO,    row.OTRO_CASO, row.TOMA_MUESTRA_LAB,  row.RESULTADO_LAB, row.TOMA_MUESTRA_ANTIGENO, row.RESULTADO_ANTIGENO,    row.CLASIFICACION_FINAL,   row.MIGRANTE,  row.PAIS_NACIONALIDAD, row.PAIS_ORIGEN,row.UCI]
        cur.execute(coredata_table_insert, data_to_upload)
        totalRowsInserted = index+1



    conn.commit()

    #getting the count AFTER inserting values for unit test purposes
    cur.execute(count_of_coretable)
    result2 = cur.fetchone()
    countAfterInserting = result2[0]
    

    controlTableValues = [countBeforeInserting, totalRows, totalRowsInserted, countAfterInserting]
    cur.execute(control_table_insert, controlTableValues)

    print("Data uploaded")
    
   
def process_data_cleansing(cur):

    print("Cleaning Data ")
    cur.execute(sp_data_cleansing)
    print("Reading complete")



if __name__ == "__main__":
    main()