# Programacion  - Trabajo Practico : Listas
#Ezequiel Gomez 

import random

print("==== EJERCICIO 1 ====")
# 1) Lista: 10 notas
notas = []
for i in range(10):
    n = float(input(f"Ingrese nota {i+1}: "))
    notas.append(n)

print("Notas ingresadas:")
for i in range(len(notas)):
    print(f"Indice {i}: {notas[i]}")

prom = sum(notas) / len(notas)
nota_max = max(notas)
nota_min = min(notas)
print("Promedio:", prom)
print("Nota mas alta:", nota_max)
print("Nota mas baja:", nota_min)

input("\nEnter para seguir...")

print("\n==== EJERCICIO 2 ====")


# 2) Lista:  5 

productos = []
for i in range(5):
    p = input(f"Ingrese producto {i+1}: ").strip()
    productos.append(p)

# Mostrar ordenados alfabeticamente 

ordenados = sorted(productos)
print("Lista ordenada:")
for i in range(len(ordenados)):
    print(ordenados[i])

elim = input("Ingrese el producto a eliminar: ").strip()
if elim in productos:
    productos.remove(elim)
    print("Lista actualizada:")
    for i in range(len(productos)):
        print(productos[i])
else:
    print("El producto no estaba en la lista.")

input("\nEnter para seguir...")

print("\n==== EJERCICIO 3 ====")


# 3) 15 numeros al azar entre 1 y 100
nums = []
for _ in range(15):
    nums.append(random.randint(1, 100))

pares = []
impares = []
for x in nums:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print("Numeros generados:")
for x in nums:
    print(x, end=" ")
print("\nPares:")
for x in pares:
    print(x, end=" ")
print("\nImpares:")
for x in impares:
    print(x, end=" ")
print("\nCantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))

input("\nEnter para seguir...")

print("\n==== EJERCICIO 4 ====")


# 4) Quitar repetidos
print("Ingrese elementos separados por espacios (ej: 1 2 2 3 4 4 5):")
entrada = input().strip().split()


# Mantener orden y quitar repetidos
sin_repetidos = []
for e in entrada:
    if e not in sin_repetidos:
        sin_repetidos.append(e)

print("Lista sin repetidos:")
for e in sin_repetidos:
    print(e, end=" ")
print()

input("\nEnter para seguir...")

print("\n==== EJERCICIO 5 ====")


# 5) Lista de 8 estudiantes
estudiantes = []
for i in range(8):
    nombre = input(f"Ingrese nombre de estudiante {i+1}: ").strip()
    estudiantes.append(nombre)

op = input("Quiere agregar (A) o eliminar (E) un estudiante? (A/E): ").strip().upper()
if op == "A":
    nuevo = input("Ingrese el nuevo estudiante: ").strip()
    estudiantes.append(nuevo)
elif op == "E":
    borrar = input("Ingrese el estudiante a eliminar: ").strip()
    if borrar in estudiantes:
        estudiantes.remove(borrar)
    else:
        print("Ese estudiante no esta en la lista.")
else:
    print("Opcion no valida, se deja la lista igual.")

print("Lista final:")
for i in range(len(estudiantes)):
    print(estudiantes[i])

input("\nEnter para seguir...")

print("\n==== EJERCICIO 6 ====")


# 6) Rotar una lista de 7 numeros a la derecha
print("Ingrese 7 numeros enteros para la lista:")
lista7 = []
for i in range(7):
    lista7.append(int(input(f"Numero {i+1}: ")))

# Rotar derecha: ultimo pasa al primero
if len(lista7) > 0:
    ultimo = lista7[-1]
    # desplazar
    for i in range(len(lista7)-1, 0, -1):
        lista7[i] = lista7[i-1]
    lista7[0] = ultimo

print("Lista rotada:")
for x in lista7:
    print(x, end=" ")
print()

input("\nEnter para seguir...")

print("\n==== EJERCICIO 7 ====")


# 7) Matriz 7x2 con min y max por dia
# temps[dia] = [min, max]
temps = []
for d in range(7):
    tmin = float(input(f"Dia {d+1} - temp minima: "))
    tmax = float(input(f"Dia {d+1} - temp maxima: "))
    temps.append([tmin, tmax])

# promedio de minimas y maximas
suma_min = 0.0
suma_max = 0.0
for par in temps:
    suma_min += par[0]
    suma_max += par[1]
prom_min = suma_min / 7
prom_max = suma_max / 7

# dia con mayor amplitud (max - min)
mayor_amp = None
dia_mayor_amp = None
for i in range(7):
    amp = temps[i][1] - temps[i][0]
    if (mayor_amp is None) or (amp > mayor_amp):
        mayor_amp = amp
        dia_mayor_amp = i + 1  # 1..7

print("Promedio de minimas:", prom_min)
print("Promedio de maximas:", prom_max)
print("Dia con mayor amplitud termica:", dia_mayor_amp, "con amplitud", mayor_amp)

input("\nEnter para seguir...")

print("\n==== EJERCICIO 8 ====")
# 8) Matriz con notas de 5 estudiantes en 3 materias
# notas[i][j] = nota del estudiante i en materia j
notas = []
for i in range(5):
    fila = []
    print(f"Estudiante {i+1}:")
    for j in range(3):
        fila.append(float(input(f"  Nota materia {j+1}: ")))
    notas.append(fila)

# promedio por estudiante
print("Promedio por estudiante:")
for i in range(5):
    prom = sum(notas[i]) / 3
    print(f"Estudiante {i+1}: {prom}")

# promedio por materia
print("Promedio por materia:")
for j in range(3):
    suma = 0.0
    for i in range(5):
        suma += notas[i][j]
    prom = suma / 5
    print(f"Materia {j+1}: {prom}")

input("\nEnter para seguir...")

print("\n==== EJERCICIO 9 ====")


# 9) Ta-Te-Ti (Tic-Tac-Toe) 3x3
tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tab):
    for fila in tab:
        print(" ".join(fila))

turno = "X"
for jugada in range(9):
    print(f"Turno de {turno}")
    mostrar_tablero(tablero)
    # pedir fila y columna 0..2
    while True:
        try:
            f = int(input("Fila (0-2): "))
            c = int(input("Columna (0-2): "))
            if 0 <= f <= 2 and 0 <= c <= 2 and tablero[f][c] == "-":
                tablero[f][c] = turno
                break
            else:
                print("Posicion invalida o ocupada. Intente otra vez.")
        except:
            print("Entrada invalida. Intente otra vez.")


    # alternar jugador
    turno = "O" if turno == "X" else "X"
    print("Tablero despues de la jugada:")
    mostrar_tablero(tablero)
    print()

print("Fin del juego.")
mostrar_tablero(tablero)

input("\nEnter para seguir...")

print("\n==== EJERCICIO 10 ====")


# 10) Ventas de 4 productos durante 7 dias -> matriz 4x7
# ventas[p][d]
ventas = []
for p in range(4):
    fila = []
    print(f"Ingrese ventas del producto {p+1} para 7 dias:")
    for d in range(7):
        fila.append(float(input(f"  Dia {d+1}: ")))
    ventas.append(fila)

# total por producto (fila)
print("Total vendido por cada producto:")
totales_producto = []
for p in range(4):
    total = sum(ventas[p])
    totales_producto.append(total)
    print(f"Producto {p+1}: {total}")

# dia con mayores ventas totales (sumar por columna)
print("Dia con mayores ventas totales:")
mejor_dia = None
mejor_total = None
for d in range(7):
    suma_dia = 0.0
    for p in range(4):
        suma_dia += ventas[p][d]
    if (mejor_total is None) or (suma_dia > mejor_total):
        mejor_total = suma_dia
        mejor_dia = d + 1
print(f"Dia {mejor_dia} con total {mejor_total}")

# producto mas vendido en la semana (mayor total por fila)
indice_mejor_producto = 0
for p in range(1, 4):
    if totales_producto[p] > totales_producto[indice_mejor_producto]:
        indice_mejor_producto = p
print(f"Producto mas vendido en la semana: Producto {indice_mejor_producto+1} con {totales_producto[indice_mejor_producto]}")

print("\nListo. Fin del practico.")