
# # anidando diccionarios
# usuarios = {
#     'diego' : {
#         "salgo": 18000,
#         "banco_asociado": "Madrid"
#     },
#     'daniel' : {
#         "salgo": 27,
#         "banco_asociado": "Facatativa"
#     }
# }

# #aqui accedemos a los datos
# for usuario in usuarios:
#     print(usuarios[usuario])

#CREANDU UN DICCIONARIO ANIDADO DE USUARIOS
usuarios = {}
usuario_activo = None
while True:
    if usuario_activo == None:
        print("")
        print("1.Crear usuario")
        print("2.Ver usuarios")
        print("3.Buscar usuario")
        print("4.salir")
        print("")
        opcion = int(input("Escoge una opcion: "))
        if opcion == 1:
            usuario = {} #creamos un diccionario interno para enviar estos datos al diccionario principal
            nombre = input("Escribe tu nombre: ")
            usuarios[nombre] = usuario # Creamos la clave que le vamos asignar al diccionario principal 
            usuario["banco_asociado"] = input("Escribe el nombre de tu banco asociado: ")
            usuario["saldo_inicial"] = int(input("Escribe tu saldo inicial"))
        elif opcion == 2:
            print(usuarios)
        elif opcion == 3:
            buscar_usuario = input("Esscribe el nombre del usuario que quiere buscar: ")
            if buscar_usuario in usuarios:
                print(usuarios[buscar_usuario]) # Del diccionario principal imprimimos la clave principal
        elif opcion == 4:
            buscar_saldo = input("Escribe el nombre de la persona: ")
            if buscar_saldo in usuarios:
                sumando = int(input("Cuanto le va a sumar? "))
                usuarios[buscar_saldo]["saldo_inicial"] += sumando # buscamos el nombre y del nombre imprimimos la informacion  
                print("Nuevo saldo:", usuarios[buscar_saldo]["saldo_inicial"])    
        elif opcion == 5:
            buscar_banco = input("Escribe el nombre de la persona para buscar del banco asociado: ")
            if buscar_banco in usuarios:
                print(usuarios[buscar_banco]["banco_asociado"])
        elif opcion == 6:
            nombre_eliminar = input("Escribe el nombre del usuario a eliminar: ")
            if nombre_eliminar in usuarios:
                del usuarios[nombre_eliminar]
                print("Usuario eliminado correctamente")
            else:
                print("Ese usuario no existe")


