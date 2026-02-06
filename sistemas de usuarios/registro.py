
# Hacer que un dicccinario de un usuario quede en una lista
usuarios = []


while True:
    print("LOGIN \n")
    print("1. Registrarse")
    print("2. Iniciar sesion ")
    print("3. Salir \n")
    try:
        opcion = int(input("Ingresa una opcion: "))
    except ValueError:
        print("Ingresa una opccion valida")

    if opcion  == 1:
        persona = {}     
        persona["nombre"] = input("Escribe tu nombre: ")
        persona["contraseña"] = input("Escribe tu pin: ")
        usuarios.append(persona)

    elif opcion == 2:
        print(usuarios)
    
            
        
    

          
                    
    


