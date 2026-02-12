print("LOGIN")

usuarios = []
opcion = 0
while True:
    print("1. Registrarse ")
    print("2. Iniciar sesion ")
    print("3. Salir ")
    while True:
        try:
            opcion = int(input("Escoge una opcion: "))
        except:
            print("Escribe una opcion valida ")
        if opcion == 1:
            existe = False
            usuario = {}
            print("Escribe los siguientes datos: ")
            usuario["nombre"] = input("Nombre: ")
            usuario["password"] = input("Escribe un pin: ")
            if usuario["nombre"] == "" or usuario["password"] == "":
                print("No se reciben espacios en blanco")
                break
            for i in usuarios:
                if usuario["nombre"] == i["nombre"]:
                    existe = True
            if existe:
                print("este nombre ya esta creado agrega otro")
            else:
                print("Se agrego correctamene!")
                usuarios.append(usuario)
                print(usuarios)
            break
        elif opcion == 2:
            print("Escribe los datos que registraste para iniciar sesion")
            try:
                nombre_ingresado = input("Nombre: ")
            except NameError:
                print("Este nombre no se encuentra registrado en el sistema registrese primero") 
                break
            contraseña_ingresada = input("Contraseña: ")
            print("usuarios guardados", usuarios)
            for i in usuarios:  
                if nombre_ingresado == i["nombre"] and contraseña_ingresada == i["password"]:
                    print("Inicio de sesion correcto")
                    print(f"Bienvenido al mundo de la proramacion {i['nombre']}")
                    print("0. Salir")
                    break
            else:
                print("Credenciales incorrectas")
                    