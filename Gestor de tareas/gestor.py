# programa que gestiona las tareas 

tareas = []

while True:
    print("GESTION DE TAREAS\n")
    print("1. agregar tareas")
    print("2. Ver tareas")
    print("3. Eliminar tareas")
    print("4. Salir")
    opcion = int(input("Escoge alguna opcion: "))
    while True:
        if opcion == 1:
            tareas.append(input("Agrega una tarea:\n "))
            print("Tarea agregada exitosamente!\n")
            volver = input("desea volver al menu principal? ")
            if volver == 's':
                print(tareas)
                break
        elif opcion == 2:
            print(tareas)
            break

        


