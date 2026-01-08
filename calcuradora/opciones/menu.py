from operaciones.operaciones_basicas import sumando, restando, multiplicando, dividiendo


def menu_opciones(op):
    if op == 1:
        num1 = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese otro numero: "))
        return sumando(num1, num2)
    elif op == 2:
        num1 = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese otro numero: "))
        return restando(num1, num2)
    elif op == 3:
        num1 = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese otro numero: "))
        return multiplicando(num1, num2)
    elif op == 4:
        num1 = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese otro numero: "))
        return dividiendo(num1, num2)  
    
    
    
    