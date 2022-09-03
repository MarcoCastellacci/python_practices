import random
nombre = input("Tu nombre es?")
class Alumno():
    
    def __init__(self, nombre, n):
        self.name = nombre
        self.nota = n
    
    def info(self):
        print("El nombre del Alumno es", self.name)
        print("Su nota es", self.nota)
    
    def notas(self):
        if self.nota >= 7:
            print(self.nota, "Has aprobado la materia")
        else:
            print(self.nota, "No alcanza para aprobar")
        

persona = Alumno(nombre, random.randint(0,10))
persona.info()
persona.notas()