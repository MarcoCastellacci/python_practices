countries = []
while True:
    country = input(f'ingresa tus Paises:')
    countries.append(country)
    print(countries)
    # Hasta aca muestra la lista completa con los paises repetidos incluidos
    if country in countries:
        countriesFiltered = set(countries)
    if len(countriesFiltered) == 5:
        #Cuando la lista de paises sin repetir llega a 5 corta el loop e imprime la lista de paises
        break

print(sorted(countriesFiltered))
