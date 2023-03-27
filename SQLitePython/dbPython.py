import sqlite3
conexion=sqlite3.connect('C:\\MorenoSan\\db\\conPython.db')
print(type(conexion))

cursor=conexion.cursor()
print(type(cursor))
sentencia='SELECT * FROM Alumnos;'
cursor.execute(sentencia)
for i in (cursor.fetchall()):
    print(i)