try:
    numero = int(input("Escribe un numero: "))
    print("El doble es:", numero * 2)
except ValueError:
    print("Eso no es un numero")

print("El programa sigue")
