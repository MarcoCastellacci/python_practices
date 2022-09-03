number = input("Elije un numero?(Debe ser un Entero)")
number = int(number)

def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "No es Numero Primo")
        break
    print(n, "Es un numero Primo")

is_prime(number)
