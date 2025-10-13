# practico4.py
#Ezequiel Gomez , materia : programacion 
# Resolución de ejercicios prácticos - Estructuras repetitivas


import random

# EJERCICIO 1: Imprimir números del 0 al 100
print("Ejercicio 1")
for i in range(101):
    print(i)

# EJERCICIO 2: Contar cantidad de dígitos de un número
print("\nEjercicio 2")
numero = int(input("Ingrese un numero entero: "))
contador = 0
num = abs(numero)
if num == 0:
    contador = 1
else:
    while num > 0:
        num = num // 10
        contador += 1
print("El numero tiene", contador, "digitos")

# EJERCICIO 3: Sumar números entre dos valores ingresados
print("\nEjercicio 3")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
suma = 0
for i in range(min(a, b)+1, max(a, b)):
    suma += i
print("La suma de los numeros entre", a, "y", b, "es", suma)

# EJERCICIO 4: Sumar números hasta ingresar 0
print("\nEjercicio 4")
total = 0
while True:
    n = int(input("Ingrese un numero (0 para terminar): "))
    if n == 0:
        break
    total += n
print("El total acumulado es", total)

# EJERCICIO 5: Adivinar un número aleatorio
print("\nEjercicio 5")
numero_aleatorio = random.randint(0,9)
intentos = 0
while True:
    intento = int(input("Adivine el numero entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        break
print("¡Correcto! Lo adivinaste en", intentos, "intentos")

# EJERCICIO 6: Números pares del 100 al 0 en orden decreciente
print("\nEjercicio 6")
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# EJERCICIO 7: Sumar números desde 0 hasta un número ingresado
print("\nEjercicio 7")
n = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(n+1):
    suma += i
print("La suma de los numeros de 0 a", n, "es", suma)

# EJERCICIO 8: Contar pares, impares, positivos y negativos
print("\nEjercicio 8")
pares = impares = positivos = negativos = 0
for i in range(100):
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# EJERCICIO 9: Calcular la media de 100 números
print("\nEjercicio 9")
suma_total = 0
for i in range(100):
    num = int(input("Ingrese un numero: "))
    suma_total += num
media = suma_total / 100
print("La media de los numeros ingresados es", media)

# EJERCICIO 10: Invertir un número
print("\nEjercicio 10")
numero = input("Ingrese un numero: ")
invertido = numero[::-1]
print("El numero invertido es", invertido)

