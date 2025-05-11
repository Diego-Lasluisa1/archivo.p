
# Listas iniciales de pasajeros y ciudades
viajeros = [
    ("Manuel Juarez", 19823451, "Liverpool"),
    ("Rosa Ortiz", 15123978, "Glasgow"),
    ("Luciana Hernandez", 38981374, "Lisboa")
]

ciudades = [
    ("Buenos Aires", "Argentina"),
    ("Glasgow", "Escocia"),
    ("Lisboa", "Portugal"),
    ("Liverpool", "Inglaterra"),
    ("Madrid", "España")    
]

# Función para agregar un pasajero
def agregar_pasajero():
    nombre = input("Ingrese el nombre del pasajero: ")
    dni = int(input("Ingrese el DNI del pasajero: "))
    destino = input("Ingrese la ciudad de destino: ")
    viajeros.append((nombre, dni, destino))
    print("Pasajero agregado correctamente.")

# Función para agregar una ciudad
def agregar_ciudad():
    ciudad = input("Ingrese el nombre de la ciudad: ")
    pais = input("Ingrese el nombre del país: ")
    ciudades.append((ciudad, pais))
    print("Ciudad agregada correctamente.")

# Función para obtener la ciudad de un pasajero según su DNI
def ciudad_por_dni():
    dni = int(input("Ingrese el DNI del pasajero: "))
    for pasajero in viajeros:
        if pasajero[1] == dni:
            print(f"El pasajero viaja a: {pasajero[2]}")
            return
    print("Pasajero no encontrado.")

# Función para contar pasajeros que viajan a una ciudad específica
def pasajeros_por_ciudad():
    ciudad = input("Ingrese el nombre de la ciudad: ")
    cantidad = sum(1 for pasajero in viajeros if pasajero[2] == ciudad)
    print(f"La cantidad de pasajeros que viajan a {ciudad} es: {cantidad}")

# Función para obtener el país de un pasajero según su DNI
def pais_por_dni():
    dni = int(input("Ingrese el DNI del pasajero: "))
    for pasajero in viajeros:
        if pasajero[1] == dni:
            destino = pasajero[2]
            for ciudad in ciudades:
                if ciudad[0] == destino:
                    print(f"El pasajero viaja a {ciudad[1]}")
                    return
    print("Pasajero o ciudad no encontrada.")

# Función para contar pasajeros que viajan a un país
def pasajeros_por_pais():
    pais = input("Ingrese el nombre del país: ")
    ciudades_en_pais = [ciudad[0] for ciudad in ciudades if ciudad[1] == pais]
    cantidad = sum(1 for pasajero in viajeros if pasajero[2] in ciudades_en_pais)
    print(f"La cantidad de pasajeros que viajan a {pais} es: {cantidad}")

# Menú iterativo
while True:
    print("\nMenú de opciones:")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Ver ciudad por DNI")
    print("4. Contar pasajeros por ciudad")
    print("5. Ver país por DNI")
    print("6. Contar pasajeros por país")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_pasajero()
    elif opcion == "2":
        agregar_ciudad()
    elif opcion == "3":
        ciudad_por_dni()
    elif opcion == "4":
        pasajeros_por_ciudad()
    elif opcion == "5":
        pais_por_dni()
    elif opcion == "6":
        pasajeros_por_pais()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente nuevamente.")
