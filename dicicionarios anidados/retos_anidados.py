# Crear usuarios (Create)

usuarios = {}

persona = {}
print("Registro de usuario")
nombre = input("Escribe tu nombre: ")
usuarios[nombre] = persona
persona["banco_asociado"] = input("banco asociado: ")
persona["saldo_inicial"] = input("Sueldo inicial: ")
print(usuarios) # imprime todos los usuarios con sus datos
print("banco asociado a la persona: ")
print(usuarios[nombre]["banco_asociado"])
print("saldo inicial de la persona: ")
print(usuarios[nombre]["saldo_inicial"])
# Actualizando el dato de la persona
nuevo_sueldo = int(input("Ingresa el nuevo calor que deseas sumar a tu saldo: "))
saldo = int(usuarios[nombre]["saldo_inicial"])
print("El nuevo saldo quedo con: ")
saldo_final = print(nuevo_sueldo + saldo)




