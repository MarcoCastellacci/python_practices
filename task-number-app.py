from functools import reduce
numbers = []

for i in range(0, 31):
    numbers.append(i)
print(numbers)

def numImpar(i):
    if i % 2:
        return True
# esta funcion separa los numeros impares y los pasa al filter    
def suma(a, b):
    return a + b
    
# esta funcion toma los numeros impares y los suma con el reduce
numeros = filter(numImpar, numbers)
print(list(numeros))

resultado = reduce(suma, numeros)
# en teoria hasta aca deberia mostrar el lsitado de numero en rango y el filtrado por impares
print(resultado)
# muestra la suma total de los numeros impares