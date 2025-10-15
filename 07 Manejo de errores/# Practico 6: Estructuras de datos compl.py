# Practico 6: Estructuras de datos complejas

# 1) Diccionario inicial y agregar frutas nuevas
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}

# 1)
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

# 3) Lista con solo las frutas 
lista_frutas = list(precios_frutas.keys())

# Mostrar resultados de 1 a 3
print("Diccionario de precios:")
print(precios_frutas)
print("Lista de frutas:")
print(lista_frutas)

# 4) Programa para almacenar y consultar numeros telefonicos
contactos = {}

print("\nCarga de 5 contactos:")
for i in range(5):
    nombre = input("Ingrese nombre del contacto: ")
    numero = input("Ingrese numero de telefono: ")
    contactos[nombre] = numero

consulta = input("\nIngrese un nombre para buscar su numero: ")

if consulta in contactos:
    print("Numero de", consulta + ":", contactos[consulta])
else:
    print("No existe un contacto con ese nombre.")

# 5) Solicitar una frase e imprimir palabras únicas y el recuento de apariciones

frase = input("Ingresá una frase: ")
palabras = frase.split()

# Palabras únicas usando un set
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# Recuento de cada palabra usando un diccionario
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Recuento:", recuento)


# 6) Ingresar nombres de 3 alumnos y sus notas, luego mostrar promedio

alumnos = {}

for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("\nPromedios:")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio}")


# 7) Conjuntos de estudiantes que aprobaron parcial 1 y 2

parcial1 = {"Ana", "Luis", "Pedro", "Maria"}
parcial2 = {"Luis", "Pedro", "Carla"}

# Ambos parciales
print("Aprobaron ambos:", parcial1 & parcial2)

# Solo uno de los dos
print("Aprobaron solo uno:", parcial1 ^ parcial2)

# Al menos uno
print("Aprobaron al menos uno:", parcial1 | parcial2)


# 8) Diccionario con stock de productos

stock = {
    "manzanas": 10,
    "bananas": 5,
    "peras": 8
}

producto = input("Ingresá el nombre del producto a consultar: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    print("El producto no existe. Se agregará al stock.")
    cantidad = int(input("Ingresá la cantidad inicial: "))
    stock[producto] = cantidad

print("Stock actualizado:", stock)


# 9) Agenda con tuplas como claves

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora: ")

actividad = agenda.get((dia, hora))
if actividad:
    print("Actividad:", actividad)
else:
    print("No hay actividad en ese horario.")


# 10) Invertir diccionario de países y capitales

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario invertido:", invertido)


