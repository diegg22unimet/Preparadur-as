# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
num = (input("Ingrese un número entero positivo: "))

if num.isnumeric():
    num = int(num)
    for i in range(1, num + 1):
        if i % 2 != 0:
            if i >= num - 1:
                print(i)
            else:
                print(i, end = ", ")
else:
    print("Entrada inválida")