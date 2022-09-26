numero = int(input("Ingrese un entero para saber si es un número primo: "))
i = 1

while i < numero:
    if numero % 2 == 0:
        print(f"{numero} no es primo")
    i += 1