# programa para controlar el flujo de los usuarios
opcion = 0
usuarios = []
usuario_activo = None
while True:
    if usuario_activo == None:
        print("---LOGIN---")
        print("1.Registrarse")
        print("2.Iniciar sesion")
        print("3. Salir")
        try:
            opcion = int(input("Escribe una opcion: "))
        except:
            print("La opcion no es correcta!")
            continue
        if opcion == 1:
            usuario = {}
            usuario["nombre"] = input("Escribe tu nombre: ")
            usuario["password"] = input("Escribe una clave:")
            usuarios.append(usuario)
            print(usuarios)
        # elif opcion == 2:
        #     print("Ingrese los datos con los que se registro")
    else:
        print("bienvenido ")
        usuario_activo = True

    