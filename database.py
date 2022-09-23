import sqlite3

database = sqlite3.connect('database.db')
database.execute("""create table if not exists Alumnos (
                    id integer primary key AUTOINCREMENT,
                    user text,
                    password text
                )""")
database.close()

conexion = sqlite3.connect("database.db")
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25))
conexion.commit()
conexion.close()

conexion=sqlite3.connect("database.db")
cursor=conexion.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(fila)
conexion.close()

def crear_usuario(usuario,password):
    conn = sqlite3.connect('mydatabase.db', isolation_level=None)
    cursor = conn.cursor()

    rows = cursor.execute(f"INSERT INTO users(name,password) VALUES('{usuario}','{password}')")
    data = rows.fetchone()

    #conn.commit() con el siolation_level no hace falta poner el commit
    cursor.close()
    conn.close()
