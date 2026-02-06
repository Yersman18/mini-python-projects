
# Hacer que un dicccinario de un usuario quede en una lista
usuarios = []
opcion = 0

while True:
    print("")
    print("LOGIN \n")
    print("1. Registrarse")
    print("2. Iniciar sesion ")
    print("3. Salir \n")
    try:
        opcion = int(input("Ingresa una opcion: "))
    except ValueError:
        print("Ingresa una opccion valida")
    if opcion == 1:
        persona = {}     
        persona["nombre"] = input("Escribe tu nombre: ")
        persona["contraseña"] = input("Escribe tu pin: ")
        for i in usuarios:
            if persona["nombre"] == i["nombre"]:
                print("Esta persona ya esta registrada")  
                break
        else:
            usuarios.append(persona)
    
    elif opcion == 2:
        print("ingrse los datos con los que ingreso")
        verificar_nombre = input("ingresa tu nombre: ")
        verificar_pin = input("ingrese su pin: ")

        for i in usuarios:
            if verificar_nombre == i["nombre"] and verificar_pin == i["contraseña"]:
                print("login exitoso")
                break
        else:
            print("Los datos son incorrectos verifique la contraseña y el usuario")
    elif opcion == 3:
        break
        

                    


