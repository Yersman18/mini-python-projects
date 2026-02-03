# creando un menu interactivo
#Menu de comidas 

menu = '''
Menu de comidas rapidas \n
1. Hamburguesas
2. Pizzas
3. Salir \n
'''

while True:
    opcion = 0
    print(menu)
    try: 
        opcion = int(input("Escribe una opcion: "))
        if opcion == 3:
            break
    except ValueError:
        print("escoge una opcion valida")
    while True:
        if opcion == 1:
            opcion_hamburguesa = 0
            print('''
                Escoga una hamburguesa \n
                1. Clasica \r
                2. Pollo
                3. Cerdo BBQ
                4. Volver al menu
                ''')
            opcion_hamburguesa = int(input("Elige alguna hamburguesa: "))
            if opcion_hamburguesa == 4:
                break
        elif opcion == 2:
            print("Estas son las opciones que tenemos de pizzas")
            print('''
                1. Pizza napolitana \r.
                2. Pizza hawaiana.
                3. Pizza marinara.
                4. Salir al menu principal''')
            opcion_pizza = 0
            opcion_pizza = int(input("cual es la pizza que deseas?"))
            if opcion_pizza == 4:
                break

            

        

   
    

    


        
