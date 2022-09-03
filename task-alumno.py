import random

class Alumno():
    nombre = "Marco"
    nota = int
    
    def notas(Alumno):
        Alumno.nota = random.randint(0,10)
        if Alumno.nota >= 7:
            print("Tu nota es", Alumno.nota)
            print(Alumno.nombre, "Has aprobado la materia")
        else:
            print("Tu nota es", Alumno.nota)
            print(Alumno.nota, "No alcanza para aprobar")

persona = Alumno()
print(persona.notas())