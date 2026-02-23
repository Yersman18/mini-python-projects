# Sistema bancario con logica real
usuario_inactivo = 0
usuarios = {}
usuario_activo = None
while True: 
    if usuario_activo == None:
        print("Sistema bancario")
        print("1. Registrarse")
        print("2. Iniciar sesion")
        print("3. Salir")
        # validando opcion
        try:
            usuario_inactivo = int(input("Escribe una opcion "))
        except: 
            print("Opcion incorrecta! Escoga nuevamene una opcion: \n")
            continue
        if usuario_inactivo > 3 or usuario_inactivo < 0:
            print("Escoge una opcion que este dentro del menu")
        
        while True:
            if usuario_inactivo ==  1:
                # REGISTRO DE USUARIO
                usuario = {}
                agregar_nombre = False
                usuario['nombre_registro'] = input("Nombre: ") # Es tipo str (string)
                print(len(usuario['nombre_registro']))
                if (usuario['nombre_registro'].isalpha()) == True:
                    usuario["nombre_registro"]
                    print("Nombre agregado")    
                else:
                    print("No es posible agregar el nombre")
                    continue
                usuario['tipo_identificacion'] = input("Tipo de identificacion: ")
                numero_registro = int(input("Numero de identiciacion: "))
                usuarios[numero_registro] = usuario 
                print(usuarios)
                print(usuarios[numero_registro])
                break
            elif usuario_inactivo == 2:
                print("---INICIO DE SESION---")
                val_identificacion = input("ingrese el tipo de identificacion: ")
                val_documento = input("ingrese su numero de identificacion: ")
                val_contraseña = input("Ingrese la  contraseña: ")    
    
            
            