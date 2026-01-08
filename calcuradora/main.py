# CALCULADORA SENCILLA
from opciones.menu import menu_opciones  

print("")
print("----CALCULADORA SENCILLA-----")
print(("1: Suma"))
print(("2: Resta"))
print(("3: Multiplicacion"))
print(("4: Division"))
print(("0: Salir"))
print("-----------------------------")

usuario = int(input("Ingrese una opcion:"))
print(menu_opciones(usuario))
salir = "no"

while salir != "si":   
    salir = input("Desea salir del programa ? ")
    if salir == "si":
        break
    print("")
    print("----CALCULADORA SENCILLA-----")
    print(("1: Suma"))
    print(("2: Resta"))
    print(("3: Multiplicacion"))
    print(("4: Division"))
    print(("0: Salir"))
    print("-----------------------------")
    usuario = int(input("Ingrese una opcion:"))
    print(menu_opciones(usuario))

    


#print(opcion)



