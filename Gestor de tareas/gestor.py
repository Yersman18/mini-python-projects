# programa que gestiona las tareas

tareas = []
opcion = 0
rango = 4

while True:
    print("GESTION DE TAREAS\n")
    print("1. Agregar tareas")
    print("2. Ver tareas")
    print("3. Eliminar tareas")
    print("4. Salir\n")
    while True:
        try:
            opcion = int(input("Escribe una opcion: "))
            break
        except ValueError:
            print("Opcion invalida")
    while True:
        if opcion > 4:
            print("La opcion no existe")
            break
        elif opcion == 1:
            rango = int(input("cuantas tareas vas agregar: "))
            for i in range(rango):
                tareas.append(input("Agrega una tarea: "))
            break
        elif opcion == 2:
            print(f"Las tareas que tenemos agregadas son: {tareas} ")
            break
        elif opcion == 3:
            num_tareas =  # Imprime el numero de las tareas
            print("Estas son las tareas que estan")
            break
                
    

            