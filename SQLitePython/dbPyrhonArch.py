import sqlite3

with sqlite3.connect('C:\\MorenoSan\\db\\conPython.db') as conexion:
    cursor=conexion.cursor()
    sentencia='SELECT * FROM Alumnos;'
    for i in (cursor.execute(sentencia).fetchmany(5)):
        print(i)