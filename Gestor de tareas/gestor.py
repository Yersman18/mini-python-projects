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
            try:          
                rango = int(input("cuantas tareas vas agregar: "))
            except:
                print("tienes que ingresar un valor correcto")
                continue
            for i in range(rango):
                tareas.append(input("Agrega una tarea: "))
            break
        elif opcion == 2:
            print(f"Las tareas que tenemos agregadas son: {tareas} ")
            break
        elif opcion == 3:
            print("Estas son las tareas que tenemos agregadas: \n")
            posicion = 0
            for tarea in tareas:
                print(f"{posicion}:{tarea}")
                posicion = posicion + 1
            eliminar = int(input("Escriba el indice de la tarea que desea eliminar: "))
            print(f"la tarea que se elimino fue {tareas[eliminar]}")
            tareas.pop(eliminar)
            print("Tarea eliminada compruebe en el sistema que se elimino")
            break                   
            
            
                
    

            