
# Hacer que un dicccinario de un usuario quede en una lista

usuarios = []


while True:
    print("LOGIN")
    print("")
    # Creando un diccionario vacio solo con las claves
    persona  = dict.fromkeys(["nombre", "contraseña"])
    # agregando datos a las claves
    persona["nombre"] = input("Escribe tu nombre: ")
    persona["contraseña"] = input("Escribe tu pin: ")
    # agregando el diccionario a una lista
    usuarios.append(persona)
    print("Registrado correctamente! Ya puedes iniciar sesion")
    while True:
        if persona["nombre"] == "" or persona["contraseña"] == "":
            print('Todos los campos son obligatorios \nRegistrate nuevamente!')
            break
