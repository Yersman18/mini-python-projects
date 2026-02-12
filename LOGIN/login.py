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
            for i in usuarios:
                if usuario["nombre"] == i["nombre"]:
                    existe = True
                           
            if existe:
                print("este nombre ya esta creado agrega otro")
            else:
                print("Se agrego correctamene!")
                usuarios.append(usuario)
            break
        elif opcion == 2:
            print("Escribe los datos que ingresaste para iniciar sesion")
            usuario["nombre"] = input("Nombre: ")
            usuario["password"] = input("Escribe un pin: ")
            for i in usuarios:
                if usuario["nombre"] == i["nombre"] and  usuario["password"] == i["password"]:
                    print("Inicio de sesion correcto")
                    print(f"Bienvenido al mundo de la proramacion {usuario['nombre']}")
                    break
            else:
                print("Credenciales incorrectas")
                    