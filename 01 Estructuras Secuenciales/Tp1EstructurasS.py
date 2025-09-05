
#Trabajo practico 1 
# #Estructura secuenciales:
# Alumno: Ezequiel Gomez  

#1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

#2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre = input ("¿cual es tu nombre?")
print(f"hola {nombre}!")

#3) Presentacion completa
nombre = input('ingrese su nombre')
apellido = input("ingrese su apellido:")
edad = input ('ingrese su edad:')
residencia = input ('¿donde vivis?')
print(f' Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}. ')

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math
radio = float(input('ingrese el radio del circulo:'))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print (f'El area es {area:2} y el perimetro es {perimetro:2}')

# 5) Crear un programa que pida al usuario una cantidad de segundos y print =total de horas:
segundos= int(input("ingrese una cantidad de segundos"))
horas= segundos/ 3600
print (f'{segundos} segundos equivalen a {horas}')

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla\
numero_a_multiplicar = int(input("Por favor, ingrese un número entero: "))
print(f"""
  {numero_a_multiplicar} x 0 = {numero_a_multiplicar * 0}
  {numero_a_multiplicar} x 1 = {numero_a_multiplicar * 1}
  {numero_a_multiplicar} x 2 = {numero_a_multiplicar * 2}
  {numero_a_multiplicar} x 3 = {numero_a_multiplicar * 3}
  {numero_a_multiplicar} x 4 = {numero_a_multiplicar * 4}
  {numero_a_multiplicar} x 5 = {numero_a_multiplicar * 5}
  {numero_a_multiplicar} x 6 = {numero_a_multiplicar * 6}
  {numero_a_multiplicar} x 7 = {numero_a_multiplicar * 7}
  {numero_a_multiplicar} x 8 = {numero_a_multiplicar * 8}
  {numero_a_multiplicar} x 9 = {numero_a_multiplicar * 9}
      """)
#7)  dos números enteros distintos del 0 
#mostrar por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingrese el primer número (≠ 0): "))
num2 = int(input("Ingrese el segundo número (≠ 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#8)Indice Masa Corporal (IMC)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc:6}")

#9)temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit
temperatura_celsius = float(input("Por favor, una temperatura en °C: "))
temperatura_fahrenheit = round((9/5)*temperatura_celsius+32, 2)
print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit} °F.")

#10 Promedio de tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio:11}")