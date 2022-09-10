def crearClass(archivo, datos):
    a = open(archivo, 'w')
    for linea in datos:
        if not linea.endswith('\n'):
            linea = linea + '\n    '         
        a.write(linea)
    a.close()

classVehiculo = [
                'class Vehiculo():',
                'color: "black"',
                'type: "coupe"',
                'year: 2008'
                    ]

crearClass('newfile.py', classVehiculo)


file = open('newfile.py', 'r' )
dato = file.read()
file.close()

print(dato)