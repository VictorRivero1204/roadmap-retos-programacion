import os

"""
Ejercicio
"""

file_name="victorrivero.txt"

with open(file_name, "w") as file:
    file.write("Victor Rivero\n")
    file.write("23\n")
    file.write("Typescript")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

"""
Extra
"""

file_name="victorrivero_tiendita.txt"

open(file_name, "a")

while True:
    print("1. Añadir producto.")
    print("2. Consultar producto.")
    print("3. Actualizar producto.")
    print("4. Borrar producto.")
    print("5. Mostrar productos.")
    print("6. Calcular ventas totales.")
    print("7. Calcular venta por producto.")
    print("8. Salir.")

    option  = input("Seleccione una opcion:")

    if option == "1":
        name  = input("nombre: ")
        quantity  = input("Cantidad: ")
        price  = input("Precio: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")
    elif option == "2":
        name  = input("nombre: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break  
    elif option == "3":
        name  = input("nombre: ")
        quantity  = input("Cantidad: ")
        price  = input("Precio: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
    elif option == "4":
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in file.readlines():
                if line.split(", ")[0] != name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")[0]
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)
    elif option == "7":
        name = input("nombre :")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")[0]
                if components[0] == name:   
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
        print(total)
    elif option == "8":
        os.remove(file_name)
        break
    else:
        print("Selecciona una de as opcionesdisponibles.")