
# nivel 1
# encendido = True

# if encendido:
#     print("Esta prendido")
# else:
#     print("Esta apagado")

# nivel 2

# numero = 10
# es_mayor = False 

# if numero > 5:
#     es_mayor = True

# print(es_mayor)

# nivel 3

# es_par = False 
# numero = 3

# if numero % 2 == 0:
#     es_par = True

# print(es_par)

# nivel 4

numeros = [20,6,8]

hay_impar = False

for i in numeros:
    residuo = i % 2
    if residuo == 1:
        hay_impar = True


if hay_impar:
    print("Hay un numero impar")
else:
    print("Todos son pares")
