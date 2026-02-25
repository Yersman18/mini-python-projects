# Sistema bancario con logica real

usuario_inactivo = 0
usuarios = {}
usuario_activo = None
while True: 
    if usuario_activo == None:
        banco = True
        print("persona no logueada")
        print("")
        print("---SISTEMA BANCARIO---")
        print("")
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
        
        elif usuario_inactivo ==  1:
            # REGISTRO DE USUARIO
            usuario = {}
            encontro = False
            numero_registro = 0
            usuario['nombre_registro'] = input("Nombre: ") # Es tipo str (string)
            if (usuario['nombre_registro'].isalpha()) == True:
                usuario["nombre_registro"]
            else:
                print("Este nombre no es valido, ingrese otro")
                continue
            while True:
                identificiones = ["cc", "ti", "ce"]
                usuario["tipo_identificacion"] = input("Tipo de identificacion: ej (cc, ti, ce): ")
                if usuario["tipo_identificacion"] in identificiones:
                    usuario["tipo_identificacion"]
                    break
                else:
                    print("Tipo de identificacion invalido")
            while True:
                try:
                    numero_registro = int(input("Numero de identificacion: "))
                except: 
                    print("Solo permite los numeros de la identificacion")
                if numero_registro in usuarios:
                    print("Esta persona ya se encuentra registrada en el sistema ingrese otro numero!") 
                    continue
                else:
                    usuarios[numero_registro] = usuario 
                    print(usuarios)
                    print("¡Se agrego al sistema!")
                    print(usuarios)
                    break

        if usuario_inactivo == 2:
            print("---INICIO DE SESION---")
            val_documento = int(input("Ingrese su numero de identificacion: "))
            if val_documento in usuarios:
                usuario_activo = val_documento
    else:
        usuario_activo = val_documento
        print("ESTE ES EL MENU DE CUENTAS DEL USARIO ")
        break


            

        

        
      
                

            