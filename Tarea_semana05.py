
# Tarea 1
clientes = {"Ana": 3300, "César": 220, "Magaly": 2354, "Julio": 450, "Irma": 1500}
while True:
    opcion = input("1. Retiro \n2. Depósito \n3. Préstamo \n4. Listar \n5. Salir \n")
    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        monto = int(input("Ingrese el monto a retirar: "))
        if nombre in clientes:
            if monto <= clientes[nombre]:
                clientes[nombre] -= monto
                print(f"{nombre} retiró {monto}")
            else:
                print(f"{nombre} no pudo retirar {monto}")
        else:
            print(f"{nombre} no existe en el diccionario")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del cliente: ")
        monto = int(input("Ingrese el monto a depositar: "))
        if nombre in clientes:
            if monto <= 2000:
                clientes[nombre] += monto
                print(f"{nombre} depositó {monto}")
            else:
                print(f"{nombre} no pudo depositar {monto}")
        else:
            print(f"{nombre} no existe en el diccionario")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del cliente: ")
        monto = int(input("Ingrese el monto de préstamo: "))
        if nombre in clientes:
            if clientes[nombre] > 2000:
                clientes[nombre] += monto
                print(
                    f"{nombre} recibió un préstamo de {monto}. Nuevo saldo: {clientes[nombre]}"
                )
            else:
                print(
                    f"{nombre} no puede recibir el préstamo porque su saldo es {clientes[nombre]}"
                )
        else:
            print(f"{nombre} no existe en el diccionario")
    elif opcion == "4":
        print(clientes)
    elif opcion == "5":
        break

# Tarea 2
alumnos = {
    "Administración": 30,
    "Contabilidad": 20,
    "Ingeniería": 27,
    "Marketing": 22,
    "Comunicación": 15,
}

while True:
    opcion = input("1. Matrícula\n2. Retiro\n3. Listar\n4. Salir\n")
    if opcion == "1":
        carrera = input("¿En qué carrera desea matricularse?: ")
        if carrera in alumnos:
            if alumnos[carrera] < 30:
                alumnos[carrera] += 1
                print(f"Matriculado en {carrera}. Total: {alumnos[carrera]}")
            else:
                print("Ya no hay plazas disponibles en esa carrera.")
        else:
            print("Carrera no encontrada.")
    elif opcion == "2":
        carrera = input("¿De qué carrera desea retirarse?: ")
        if carrera in alumnos:
            if alumnos[carrera] > 0:
                alumnos[carrera] -= 1
                print(f"Retiro realizado en {carrera}. Total: {alumnos[carrera]}")
            else:
                print("No hay alumnos para retirar en esa carrera.")
        else:
            print("Carrera no encontrada.")
    elif opcion == "3":
        print(alumnos)

    elif opcion == "4":
        break


# Tarea 3
inventario = {
    "Cien Años de Soledad": 5,
    "El Principito": 8,
    "Don Quijote": 3,
    "Harry Potter": 10,
    "Mafalda": 4,
}

while True:
    opcion = input("\n1. Vender\n2. Comprar\n3. Listar\n4. Salir\n")
    if opcion == "1":
        libros = list(inventario.keys())
        for i, nombre in enumerate(libros, 1):
            print(f"{i}. {nombre}")
        num = int(input("Elige el número del libro a vender: "))
        libro = libros[num - 1]
        if inventario[libro] > 0:
            inventario[libro] -= 1
            print(f"Libro vendido: {libro}. Stock restante: {inventario[libro]}")
        else:
            print("No hay stock disponible.")
    elif opcion == "2":
        libros = list(inventario.keys())
        for i, nombre in enumerate(libros, 1):
            print(f"{i}. {nombre}")
        num = int(input("Elige el número del libro a comprar: "))
        libro = libros[num - 1]
        cantidad = int(input("¿Cuántas unidades desea comprar?: "))
        inventario[libro] += cantidad
        print(f"Libro comprado: {libro}. Stock total: {inventario[libro]}")
    elif opcion == "3":
        print(inventario)
    else:
        break
