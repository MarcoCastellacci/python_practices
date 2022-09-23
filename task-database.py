import sqlite3

def main():
    nombre = input('Nombre del Alumno: ')

    if buscar_alumno(nombre):
        print('Alumno Encontrado')
    else:
        print('No Hay Alumno')
def buscar_alumno(nombre):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    rows = cursor.execute(f"SELECT * FROM Alumnos WHERE name='{nombre}'")
    data = rows.fetchone()
    print(data)

    cursor.close()
    conn.close()

    if data == None:
        return False
    return True

if __name__ == '__main__':
    main()
