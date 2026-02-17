# Esto es un sistema bancario 

opcion = 0
bancario = True # Controla el flujo del programar para poder salir del sistema 
usuarios = []
usuario_actual = None

while bancario:
    if usuario_actual == None:
        print("Usuario no logueado")       
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
        if opcion > 3 or opcion < 0:
            print("No existe esta opcion, escoga una opcion valida")
        elif opcion  == 1:
            existe = False
            usuario = {}
            print("")
            print("---REGISTRO DE USUARIO---")
            print("")
            print("Registre los siguientes datos:\n")
            usuario["nombre"] = input("Nombre: ")
            usuario["password"] = input("Pin: ")
            if usuario["nombre"].isalpha() == False: # tambien nos controla los espacios y no los tomas como STRING
                print("Este nombre no es valido, para el registro ")
                continue
            for i in usuarios:
                if usuario["nombre"] == i["nombre"]:
                    existe = True
                    if existe:
                        print("Este nombre ya esta agregado al sistema!")
                        break     
            else:
                usuarios.append(usuario)
                print("La persona fue agregada al sistema!")
        elif opcion == 2:
            print("")
            print("---INICIO DE SESION---")
            print("")
            print("Ingrese los con los que se registro: ")
            nombre_ingresado = input("Ingrese su nombre: ")  
            pin_ingresado = input("Ingrese su pin: " )
            usuario_logueado = int(input("Escribe un opcion: "))
            for j in usuarios:
                if nombre_ingresado == j["nombre"] and pin_ingresado == j["password"]: 
                    print(f"Bienvenido {j['nombre']}, esta en el menu bancario")
                    usuario_actual = j
                    break                            
            else:
                print("te equivocaste")
        elif opcion == 3:
            bancario =  input("Esta seguro que quiere salir del sistema?")
            if bancario  == "si":
                print("Gracias por su atencion")
                usuario_actual = None
        elif opcion == 0:
            print(usuarios)
    else:
        print("---SISTEMA BANCARIO---")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Salir")
        if usuario_logueado == 1:
            print("El saldo que tienes es de 00000") # solo es de muestra
        elif usuario_logueado == 3:
            print("Ha cerrado sesion correctamente ")
            usuario_actual = None
            break  
          

        

        