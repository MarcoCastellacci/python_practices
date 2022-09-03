class Vehiculo():
    color = "Negro"
    Ruedas = 4
    Puertas = 5
    
class Coche(Vehiculo):
    Velocidad = "100km/h"
    Cilindrada = "V8"
    
auto = Coche()

print(auto.color, auto.Ruedas, auto.Puertas, auto.Velocidad, auto.Cilindrada)