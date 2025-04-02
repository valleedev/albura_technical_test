#para ejecutar este navegue hasta la carpeta CRUD y ejecute python main.js

from os import system
array = []
max_size = 10

def fill_array():
    while len(array) < max_size:
        value = input(f"Ingrese un valor ({len(array) + 1}/{max_size}): ")
        if value.strip():
            array.append(value)
    print("Array completo:", array)

def menu():
    system("cls")
    option = ""
    while option != "5":
        print("\nSeleccione una opción:")
        print("1- Añadir un elemento")
        print("2- Eliminar un elemento")
        print("3- Modificar un elemento")
        print("4- Listar elementos")
        print("5- Salir")
        option = input("Ingrese su opción: ")
        
        if option == "1":
            add_element()
        elif option == "2":
            remove_element()
        elif option == "3":
            modify_element()
        elif option == "4":
            list_elements()
        elif option == "5":
            print("Saliendo...")
        else:
            print("Opción inválida, intente de nuevo.")

def add_element():
    if len(array) < max_size:
        value = input("Ingrese un valor a añadir: ")
        if value.strip():
            array.append(value)
            print("Elemento añadido.", array)
    else:
        print("El array ya está lleno.")
        input()

def remove_element():
    try:
        index = int(input(f"Ingrese la posición a eliminar (0 - {len(array) - 1}): "))
        if 0 <= index < len(array):
            del array[index]
            print("Elemento eliminado.", array)
        else:
            print("Índice inválido.")
    except ValueError:
        print("Ingrese un número válido.")

def modify_element():
    try:
        index = int(input(f"Ingrese la posición a modificar (0 - {len(array) - 1}): "))
        if 0 <= index < len(array):
            new_value = input("Ingrese el nuevo valor: ")
            if new_value.strip():
                array[index] = new_value
                print("Elemento modificado.", array)
        else:
            print("Índice inválido.")
    except ValueError:
        print("Ingrese un número válido.")

def list_elements():
    print("Elementos del array:", array)

fill_array()
menu()
