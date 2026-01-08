# CALCULADORA SENCILLA

from operaciones.operaciones_basicas import restando, sumando, dividiendo, multiplicando

print("")
print("----CALCULADORA SENCILLA-----")
print(("1: Suma"))
print(("2: Resta"))
print(("3: Multiplicacion"))
print(("4: Division"))
print("-----------------------------")

usuario = int(input("Escriba una opcion: "))

if usuario == 1:
    print("ingresa dos numeros")
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    resultado = (restando(numero1, numero2))
    print(resultado)
elif usuario == 2:
    print("ingresa dos numeros")
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    resultado = (sumando(numero1, numero2))
    print(resultado)
elif usuario == 3:
    print("ingresa dos numeros")
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    resultado = (dividiendo(numero1, numero2))
    print(resultado)
elif usuario == 4:
    print("ingresa dos numeros")
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    resultado = (multiplicando(numero1, numero2))
    print(resultado)

#print(opcion)



