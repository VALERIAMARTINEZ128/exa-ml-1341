
# Valeria Yaretzi - NC: 1341
# Programa de bibliotecas utilizando diccionarios
# numero de problema 36 
datos_bibliotecas = {
    "Biblioteca": ["Vasconcelos", "México", "Lerdo",
                   "Bellas Artes", "Central", "Infantil"],
    "Libros": [600000, 450000, 280000, 150000, 320000, 50000],
    "Usuarios_dia": [3500, 2800, 1500, 1200, 2200, 800]
}

while True:
    print("\n===== SISTEMA DE BIBLIOTECAS =====")
    print("1. Mostrar todas las bibliotecas")
    print("2. Buscar una biblioteca")
    print("3. Agregar una biblioteca")
    print("4. Mostrar total de libros")
    print("5. Mostrar total de usuarios por día")
    print("6. Salir")
    print("elaborado por valeria yaretzi NC = 1341 ")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("\nLISTA DE BIBLIOTECAS")

        for i in range(len(datos_bibliotecas["Biblioteca"])):
            print("\nBiblioteca:", datos_bibliotecas["Biblioteca"][i])
            print("Libros:", datos_bibliotecas["Libros"][i])
            print("Usuarios por día:",
                  datos_bibliotecas["Usuarios_dia"][i])

    elif opcion == "2":
        nombre = input("Escribe el nombre de la biblioteca: ")
        encontrada = False

        for i in range(len(datos_bibliotecas["Biblioteca"])):
            if datos_bibliotecas["Biblioteca"][i].lower() == nombre.lower():
                print("\nBiblioteca encontrada")
                print("Nombre:", datos_bibliotecas["Biblioteca"][i])
                print("Libros:", datos_bibliotecas["Libros"][i])
                print("Usuarios por día:",
                      datos_bibliotecas["Usuarios_dia"][i])
                encontrada = True

        if encontrada == False:
            print("La biblioteca no existe.")

    elif opcion == "3":
        nombre = input("Nombre de la nueva biblioteca: ")
        libros = int(input("Cantidad de libros: "))
        usuarios = int(input("Usuarios por día: "))

        datos_bibliotecas["Biblioteca"].append(nombre)
        datos_bibliotecas["Libros"].append(libros)
        datos_bibliotecas["Usuarios_dia"].append(usuarios)

        print("Biblioteca agregada correctamente.")

    elif opcion == "4":
        total_libros = sum(datos_bibliotecas["Libros"])
        print("Total de libros:", total_libros)

    elif opcion == "5":
        total_usuarios = sum(datos_bibliotecas["Usuarios_dia"])
        print("Total de usuarios por día:", total_usuarios)

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
