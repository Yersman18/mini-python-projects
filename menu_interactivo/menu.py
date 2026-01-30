# creando un menu interactivo
#Menu de comidas 

menu = '''
Menu de comidas rapidas \n
1. Hamburguesas
2. Pizzas
3. Perros calientes
4. Mazorcadas
5. Salir \n
'''
hamburguesas =  ( '''
Escoga una hamburguesa \n
1. Clasica
2. Pollo
3. Cerdo BBQ
4. Volver al menu
''')

while True:
    opcion = 0
    print(menu)
    try: 
        opcion = int(input("Escribe una opcion: "))
    except ValueError:
        print("escoge una opcion valida")
    if opcion == 1:
        volver = print(menu)
        opcion_hamburguesa = 0
        print(hamburguesas)
        opcion_hamburguesa = int(input("Elige alguna hamburguesa: "))
        if opcion_hamburguesa == 4:
            volver = input("estas seguro de volver al menu?")
            if volver == "s":
                print(menu)
    if opcion == 5:
        opcion = input("Estas seguro de salir del sistema? ")
        if opcion == "s":
            break
                    

        

   
    

    


        
