
# Hacer que un dicccinario de un usuario quede en una lista

usuarios = []
persona  = dict.fromkeys(["nombre", "contraseña"])
opcion = 0

while True:
    print("LOGIN \n")
    print("1. Registrarse")
    print("2. Iniciar sesion ")
    print("3. Salir \n")
    while True:
        try:
            opcion = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Ingresa una opccion valida")
        break
    if opcion  == 1: 
            # Creando un diccionario vacio solo con las claves
            # agregando datos a las claves
            persona["nombre"] = input("Escribe tu nombre: ")
            persona["contraseña"] = input("Escribe tu pin: ")
            if persona["nombre"] == "" or persona["contraseña"] == "":
                print("Todos los campos son obligatorios\n")
            else:
                usuarios.append(persona)
                print("Agregado correctamente")
                break
    
print(usuarios)

print(type(usuarios))