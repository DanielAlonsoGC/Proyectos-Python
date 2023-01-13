from random import *
print("----JUEGO ADIVINA EL NUMERO----")
nombre = input("Bienvenido cual es tu nombre: \n")
num_pensado = randint(1, 100)
pregunta = """ #He pensado en un numero.
#Te reto adivinar cual es, solo tienes 8 intentos \n"""
num_usuario = int(input(pregunta))
# termina el juego: cuando se pasa de los 8 intentos o adivina
lista = list(range(1, 9))
for indice, item in enumerate(lista):
    up_indice = indice + 1
    if num_usuario < 1:
        num_usuario = int(input("!ERROR! Digite otro numero mayor a 1\n"))
    if num_usuario > 100:
        num_usuario = int(input("!ERROR! Digite otro numero menor a 100\n"))
    if num_usuario < num_pensado:
        num_usuario = int(input("Respuesta incorrecta!\nDigite un numero mayor\n"))
    if num_usuario > num_pensado:
        num_usuario = int(input("Respuesta incorrecta!\nDigite un numero menor\n"))
    if num_usuario == num_pensado:
        print("Respuesta correcta")
        print(f"El numero pensado era {num_pensado} , usted lo adivino en {up_indice} intentos")
        break
if num_pensado != num_usuario:
     print(f'PERDISTE! Se agotaron los intentos el numero era {num_pensado}')







