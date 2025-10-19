# Programación I - TP2: Funciones en Python
# Alumno: Ezequiel Gomez

import math

def imprimir_hola_mundo():
    "Imprime 'Hola Mundo!' por pantalla."
    print("Hola Mundo!")

def saludar_usuario(nombre):
    "Devuelve un saludo personalizado con el nombre recibido."
    return f"¡Hola {nombre}!"

def informacion_personal(nombre, apellido, edad, residencia):
    "Imprime una presentación con los datos personales."
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def calcular_area_circulo(radio):
    "Devuelve el área de un círculo a partir de su radio."
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    "Devuelve el perímetro de un círculo a partir de su radio."
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    "Convierte una cantidad de segundos a horas (valor decimal).
    return segundos / 3600

def tabla_multiplicar(numero):
    "Imprime la tabla de multiplicar del número del 1 al 10."
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def operaciones_basicas(a, b):
    "Devuelve una tupla con (suma, resta, multiplicación, división).
    Si b = 0, la división se devuelve como None."
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return (suma, resta, multiplicacion, division)

def calcular_imc(peso, altura):
    "Devuelve el Índice de Masa Corporal (IMC)."
    return peso / (altura ** 2)

def celsius_a_fahrenheit(celsius):
    "Convierte grados Celsius a Fahrenheit."
    return (9/5) * celsius + 32

def calcular_promedio(a, b, c):
    "Devuelve el promedio de tres números."
    return (a + b + c) / 3

# ---------------- Programa principal ----------------
if __name__ == "__main__":
    print("====")
    print("   TP2 - Funciones en Python")
    print("   Alumno: Ezequiel Gomez")
    print("====\n")

    # 1) Hola Mundo
    imprimir_hola_mundo()
    print()

    # 2) Saludo personalizado
    nombre = input("2) Ingresá tu nombre: ")
    print(saludar_usuario(nombre))
    print()

    # 3) Información personal
    n = input("3) Nombre: ")
    a = input("   Apellido: ")
    e = input("   Edad: ")
    r = input("   ¿Dónde vivís?: ")
    informacion_personal(n, a, e, r)
    print()

    # 4) Área y perímetro del círculo
    try:
        radio = float(input("4) Ingresá el radio de un círculo: "))
        area = calcular_area_circulo(radio)
        perimetro = calcular_perimetro_circulo(radio)
        print(f"   Área: {area:.2f}")
        print(f"   Perímetro: {perimetro:.2f}")
    except ValueError:
        print("   Dato inválido: el radio debe ser numérico.")
    print()

    # 5) Segundos a horas
    try:
        segundos = int(input("5) Ingresá una cantidad de segundos: "))
        horas = segundos_a_horas(segundos)
        print(f"   {segundos} segundos equivalen a {horas:.2f} horas.")
    except ValueError:
        print("   Dato inválido: los segundos deben ser un número entero.")
    print()

    # 6) Tabla de multiplicar
    try:
        numero_tabla = int(input("6) Ingresá un número para ver su tabla (1 al 10): "))
        tabla_multiplicar(numero_tabla)
    except ValueError:
        print("   Dato inválido: debe ser un número entero.")
    print()

    # 7) Operaciones básicas
    try:
        a = float(input("7) Primer número: "))
        b = float(input("   Segundo número: "))
        suma, resta, mult, div = operaciones_basicas(a, b)
        print(f"   Suma: {suma}")
        print(f"   Resta: {resta}")
        print(f"   Multiplicación: {mult}")
        if div is None:
            print("   División: no se puede dividir por cero.")
        else:
            print(f"   División: {div}")
    except ValueError:
        print("   Dato inválido: deben ser números.")
    print()

    # 8) IMC
    try:
        peso = float(input("8) Ingresá tu peso en kg: "))
        altura = float(input("   Ingresá tu altura en metros: "))
        imc = calcular_imc(peso, altura)
        print(f"   Tu IMC es: {imc:.2f}")
    except ValueError:
        print("   Dato inválido: peso y altura deben ser numéricos.")
    print()

    # 9) Celsius a Fahrenheit
    try:
        c = float(input("9) Ingresá la temperatura en °C: "))
        f = celsius_a_fahrenheit(c)
        print(f"   {c:.2f} °C equivalen a {f:.2f} °F.")
    except ValueError:
        print("   Dato inválido: la temperatura debe ser numérica.")
    print()

    # 10) Promedio de tres números
    try:
        x = float(input("10) Número 1: "))
        y = float(input("    Número 2: "))
        z = float(input("    Número 3: "))
        promedio = calcular_promedio(x, y, z)
        print(f"   El promedio es: {promedio:.2f}")
    except ValueError:
        print("   Dato inválido: ingresá números (pueden tener decimales).")
    print("\nFin del TP2. ¡Gracias!")
