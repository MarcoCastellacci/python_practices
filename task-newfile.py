file = open('newfile.txt', 'w' )
file.write('HOla Mundo\n')
file.write('New Scripts\n')
file.close()

file = open('newfile.txt', 'r' )
dato = file.read()
file.close()

print(dato)





# r = leer
# w = escribir // se sobreescriben los datos del archivo
# a = append (agregar) // se agreaga al final del archivo
# x = crear // se supone automatico, pero sino existe se crea el archivo 

# t = texto
# b = binario
# +