año = input('Entre el año a verificar (4 digitos)')
año = int(año)

def año_bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "Es un año bisiesto")
    else:
        print(year, "No es año Bisiesto")
        
año_bisiesto(año)
