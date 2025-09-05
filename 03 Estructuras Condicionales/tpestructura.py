##Práctico 3: Estructuras condicionales

# 1 Edad
# Se solicita al usuario que ingrese su edad, si la edad es mayor o igual
#que 18 se imprime en pantalla "mayor de edad " ejercicio:

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

#2 Nota del Usuario:
# si la nota que recibe el usuario es mayor o igual a 6 esta aprobado
#si la nota es menor a 6 esta desaprobado. ejercicio:
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Número par 
# El número es par si numero % 2 == 0. se solicita numero y se verifica 
#ejemplo: 

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4 categorias x edad : 
#Para identificar las categorias usamos if-elif-else.
#Ejemplo: 
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5 Contrasena correcta:
#revisamos si la contrasena esta entre 8 y 14 caracteres 
password = input("Ingrese su contraseña: ")
if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6 Sesgo de una lista de números
#Usamos statistics para calcular media, mediana y moda.
# comparamos:
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

m = mean(numeros_aleatorios)
med = median(numeros_aleatorios)
mod = mode(numeros_aleatorios)

if m > med > mod:
    print("Sesgo positivo")
elif m < med < mod:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

#7 Frase terminada en vocal :
#verificamos la ultima letra del string 

frase = input("Ingrese una frase : ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

#8 Transformacion del nombre 
#Dependiendo de la opcion que elija el usuario cambiamos Mayuscula de miusculas

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 (mayúsculas), 2 (minúsculas), 3 (primera letra mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

#9) Magnitud de terremoto
#Clasificacion y su devolucion:
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

#10 Estacion segun hemisferio y fecha 
# A continuacion pedimos fechas ! 
 
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:  # Hemisferio sur
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print("La estación es:", estacion)








