# Esto es un sistema bancario 

opcion = 0
bancario = True # Controla el flujo del programar para poder salir del sistema 
usuarios = []
while bancario:
    print("")
    print("--- BANCON PYTHON ---")
    print("")
    print("1. Registrarse")
    print("2. Iniciar sesion")
    print("3. Salir\n")
    try:
        opcion = int(input("Escoge una opcion: "))
    except:
        print("La opcion que escogiste no es valida")
        continue
    if opcion > 3:
        print("No existe esta opcion, escoga una opcion valida")
    elif opcion  == 1:
        numero = False
        usuario = {}
        print("")
        print("---REGISTRO DE USUARIO---")
        print("")
        print("Registre los siguientes datos:\n")
        usuario["nombre"] = input("Nombre: ")
        if usuario["nombre"].isnumeric() == True:
            print("Este nombre no es valido, para el registro ")
        else:
            usuarios.append(usuario)
            print(usuarios)
            print("La persona fue agregada al sistema!")
        

        
