# GRANT/REVOKE ACCESS

sp_grant_access = "CALL udacitydata.grantAccess()"
sp_revoke_access = "CALL udacitydata.revokeAccess()"

#STORED PROCEDURES

sp_data_cleansing = "CALL udacitydata.coredata_cleansing()"


#DELETE

coredata_table_delete = "DELETE FROM udacitydata.coredata"


#INSERTING


entidades_table_insert = ("""INSERT INTO udacitydata.entidades( 
id, 
entidad_federativa, 
abreviatura) 
VALUES (%s, %s, %s);""")


municipios_table_insert = ("""INSERT INTO udacitydata.municipios(
	id, 
	municipio, 
	clave_entidad
	)
	VALUES (%s, %s, %s);""")


nacionalidad_table_insert = ("""INSERT INTO udacitydata.nacionalidad(
	id, "descripcion")
	VALUES (%s, %s);""")

clasificacion_table_insert = ("""INSERT INTO udacitydata.clasificacion(
	id, 
	clasificacion, 
	descripcion)
	VALUES (%s, %s, %s);""")

coredata_table_insert = ("""INSERT INTO udacitydata.coredata(
	fecha_actualizacion, id_registro, origen, sector, entidad_um, sexo, entidad_nac, entidad_res, municipio_res, tipo_paciente, fecha_ingreso, fecha_sintomas, fecha_def, intubado, neumonia, edad, nacionalidad, embarazo, habla_lengua_indig, indigena, diabetes, epoc, asma, inmusupr, hipertension, otra_com, cardiovascular, obesidad, renal_cronica, tabaquismo, otro_caso, toma_muestra_lab, resultado_lab, toma_muestra_antigeno, resultado_antigeno, clasificacion_final, migrante, pais_nacionalidad, pais_origen, uci)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""")

origen_table_insert = ("""INSERT INTO udacitydata.origen(
	id, descripcion)
	VALUES (%s, %s);""")

resultadoantigeno_table_insert = ("""INSERT INTO udacitydata.resultadoantigeno(
	id, descripcion)
	VALUES (%s, %s);
""")

resultadolab_table_insert = ("""INSERT INTO udacitydata.resultadolab(
	id, descripcion)
	VALUES (%s, %s);""")

sector_table_insert = ("""INSERT INTO udacitydata.sector(
	id, descripcion)
	VALUES (%s, %s);""")

sexo_table_insert = ("""INSERT INTO udacitydata.sexo(
	id, descripcion)
	VALUES (%s, %s);""")

sionocatalog_table_insert = ("""INSERT INTO udacitydata.sionocatalog(
	id, descripcion)
	VALUES (%s, %s);""")

tipodepaciente_table_insert = ("""INSERT INTO udacitydata.tipodepaciente(
	id, descripcion)
	VALUES (%s, %s);""")

control_table_insert = ("""INSERT INTO udacitydata.controlTable(
	countBeforeInserting, toInsert, realValue, countAfterInserting)
	VALUES (%s, %s, %s, %s);""")

count_of_coretable = ("""SELECT COUNT(*) FROM udacitydata.coredata""")
