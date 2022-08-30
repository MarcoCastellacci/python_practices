# las listas no son inmutables y van entre []

lista = [1, 2, 3, 4]
# print(lista)
lista[0] = "0"
# print(lista)
lista.append("a")
lista.append("b") 
print(lista)
# append puede agregar a la lista
lista.remove("a")
lista.remove(2)
# remove elimina elementos de la lista
print(lista)

# las tuple son inmutables y van entre ()

tuple = (1, 2, 3, 4, 5, 6, 7, 8)
# print(tuple)
# tuple[0] = "a"
# tuple[9] = "b"
# print(tuple) 
# esto da un error y no modifica la tuple cualquiera de los dos casos - la tuple es el equivalente a una const 

# diccionario de python son como los json
diccionario = {
    "a": 1,
    "b": 2,
    "c": "hola"
}
print(diccionario)
print(diccionario["a"])
diccionario["b"] = {"a": 1, "b": 2}
print(diccionario)

elementoViejo = diccionario.pop("c")
print(diccionario)
print(elementoViejo)

# conjuntos o sets no pueden tener elementos duplicados
lista = [ 1, 2, 3, 1, 2, 3, 2, 3,]
conjunto = {1, 2, 3, 1, 4, 2, 3, 1, 2}
print(lista)
print(conjunto)
# los conjuntos pueden unirse manteniendo su estructura no repetitiva
a = {1, 2, 3, 1, 4, 2, 3, 1}
b = {1, 2, 5, 6, 7 ,4, 9, 1}
print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(a^b)
# falta diferencia simetrica que devuelve los datos que no se repitan en ninguna de los dos conjuntos





