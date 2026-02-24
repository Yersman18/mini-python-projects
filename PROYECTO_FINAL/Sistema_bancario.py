# Sistema bancario con logica real
from xmlrpc.client import boolean


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
                encontro = False
                numero_registro = 0
                usuario['nombre_registro'] = input("Nombre: ") # Es tipo str (string)
                print(len(usuario['nombre_registro']))
                if (usuario['nombre_registro'].isalpha()) == True:
                    usuario["nombre_registro"]
                else:
                    print("Este nombre no es valido, ingrese otro")
                    continue
                while True:
                    identificiones = ["cc", "ti", "ce"]
                    usuario["tipo_identificacion"] = input("Tipo de identificacion: ej (cc, ti, ce) ")
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
                    
                    usuarios[numero_registro] = usuario 
                    print(usuarios)
                    print("¡Se agrego al sistema!")
                    break
            break
        if usuario_inactivo == 2:
            print("---INICIO DE SESION---")
            # vamos para verificar los datos que registro en el sistema
            val_identificacion = input("ingrese el tipo de identificacion: ")
            val_documento = int(input("ingrese su numero de identificacion: "))
            val_nombre = input("Ingrese el nombre: ")
            if val_documento in usuarios:
                print(val_nombre == usuarios[numero_registro]['nombre_registro'])   
        elif usuario_inactivo == 0:
            print(usuarios)  
        
            