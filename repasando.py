# gestor de tareas 

lista_tareas = []
opcion = 0
while True:
    print("")
    print("Gestor de tareas\n" )
    print("1.Agregar")
    print("2.Ver tareas")
    print("3. Salir\n")
    opcion = int(input("Escoge una opcion: "))
    if opcion == 3:
        salir = input("Esta seguro salir del sistema? ")
        if salir == "si":
            break
    while True:
        if opcion == 1:
            tarea = input("Agrega una tarea: ")
            lista_tareas.append(tarea)
            volver = input("Quiere agregar otra tarea? ")
            if volver == "no":
                break
        elif opcion == 2:
            print("Tareas agregadas: \n")
            for i in lista_tareas:
                print(i)
            break 
    

