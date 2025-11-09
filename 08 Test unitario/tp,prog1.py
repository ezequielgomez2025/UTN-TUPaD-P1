#!/usr/bin/env python3

from pathlib import Path

ARCHIVO = "productos.txt"
# archivo inicial automáticamente si no existe

def crear_archivo_si_no_existe():
    ruta = Path(ARCHIVO)
    if not ruta.exists():
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.write("Pelota Adidas,25000,10\n")
            f.write("Botines Nike,48000,5\n")
            f.write("Camiseta Titular,35000,8\n")

# Leer productos desde archivo

def leer_productos():
    productos = []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            nombre, precio, cantidad = linea.strip().split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
    return productos



# Mostrar productos

def mostrar_productos(productos):
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")



# Agregar producto

def agregar_producto():
    print("\n--- Agregar producto ---")
    nombre = input("Nombre: ").strip()
    precio = input("Precio: ").strip()
    cantidad = input("Cantidad: ").strip()

    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{precio},{cantidad}\n")

    print("Producto agregado correctamente.")



# Guardar productos sobrescribiendo todo

def guardar_productos(productos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Cambios guardados.")


# Buscar producto por nombre

def buscar_producto(productos, nombre):
    for p in productos:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None



# Menú principal

def menu():
    crear_archivo_si_no_existe()  

    productos = leer_productos()

    while True:
        print("\n1) Listar productos")
        print("2) Agregar producto")
        print("3) Buscar producto")
        print("4) Guardar cambios")
        print("0) Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            mostrar_productos(productos)

        elif opcion == "2":
            agregar_producto()
            productos = leer_productos()  # recarga para mantener sincronizado

        elif opcion == "3":
            nombre = input("Ingrese nombre a buscar: ").strip()
            encontrado = buscar_producto(productos, nombre)
            if encontrado:
                print(f"Encontrado → Nombre: {encontrado['nombre']}, Precio: ${encontrado['precio']}, Cantidad: {encontrado['cantidad']}")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            guardar_productos(productos)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
