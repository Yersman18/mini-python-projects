# Sistema bancario con logica real

usuario_inactivo = 0
usuarios = {}
usuario_activo = None
banco = True
while banco: 
    if usuario_activo == None:
        banco = True
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
                    print("¡Se agrego al sistema!")
                    break

        if usuario_inactivo == 2:
            print("---INICIO DE SESION---")
            val_documento = int(input("Ingrese su numero de identificacion: "))
            if val_documento in usuarios:
                usuario_activo = val_documento
                nombre_usuario = usuarios[val_documento]['nombre_registro']
            else:
                print('''Credenciales incorrectas''')            
    else:
     cuentas_usuario = {}# almacena las cuentas 
     if usuario_activo == val_documento:
        print("")
        print (f"Bienvenido {usuarios[val_documento]['nombre_registro']}!")
        print("")
        print("Tipos de cuenta:")
        print("1. Crear cuenta")
        print("2. Consultar cuentas")
        print("3. Salir")
        print("")
        usuario_opcion = 0
        cuentas = {}
        try:
            usuario_opcion = int(input("Elige una opcion: "))
        except:
            print("Esta opcion no es valida")
            continue
        while usuario_activo == val_documento:
            if usuario_opcion == 1:
                print("")
                print("---CREAR CUENTA---\n")
                print("Que cuenta quiere abrir: ")
                print("1.Abrir cuenta de ahorros")
                print("2.Abrir cuenta corriente")
                print("0.Salir")
                try:
                    usuario_cuenta = int(input("Elige un opcion: "))
                except:
                    print("Escriba una opcion valida")
                    continue              
                if usuario_cuenta == 1:
                    cuenta_ahorro = {}
                    cuenta_ahorro['nombre_cuenta'] = input("Escriba un nombre para su cuenta: ")
                    cuenta_ahorro['correo'] = (input("Escribe tu correo electronico: "))
                    cuenta_ahorro['saldo_inicial'] = int(input("Escribe el saldo inicilal:   "))
                    cuentas["cuenta_ahorro"] = cuenta_ahorro # agrega la cuenta a cuentas
                    
                elif usuario_cuenta == 2:
                    cuenta_corriente = {}
                    cuenta_corriente['nombre_cuenta_corriente'] = input("Escriba su nombre completo: ")
                    cuenta_corriente["correo_cuenta_corriente"] = input("escriba su correo eletronico:")
                    cuenta_corriente["suelddo_iniicial_corriente"] = (input("Escriba su sueldo inicial"))
                    cuentas["cuenta_Corriente"] = cuenta_corriente
            
                elif usuario_cuenta == 0:
                    print(cuentas)
            elif usuario_opcion == 2:
                print(cuentas)
            elif usuario_opcion == 3:
                print("Ha cerrado sesion!")
                usuario_activo = None

                