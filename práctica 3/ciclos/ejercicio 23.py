#Hacer un programa que permita al usuario jugar al piedra, papel o tijera contra la computadora.
#se debe jugar al mejor de 5, es decir, si uno de los participantes consigue 3 victorias el
#juego termina.

import random

lista=["piedra", "papel","tijera"]

cont_maquina=0
cont_usuario=0

bandera=True

while bandera:
    usuario=input("piedra, papel o tijera?\nel usuario eligió: ")
    maquina=random.choice(lista)

    if maquina=="piedra" and usuario=="tijera":
        cont_maquina+=1
        print("la maquina eligio: ", maquina)
        print("punto para la máquina")
    elif maquina=="tijera" and usuario=="papel":
        cont_maquina+=1
        print("la maquina eligio: ", maquina)
        print("punto para la máquina")

    elif maquina=="papel" and usuario=="piedra":
        cont_maquina+=1
        print("la maquina eligio: ", maquina)
        print("punto para la máquina")


    if usuario=="piedra" and maquina=="tijera":
        cont_usuario+=1
        print("la maquina eligio: ", maquina)
        print("punto para el usuario")

    elif usuario=="tijera" and maquina=="papel":
        cont_usuario+=1
        print("la maquina eligio: ", maquina)
        print("punto para el usuario")

    elif usuario=="papel" and maquina=="piedra":
        cont_usuario+=1
        print("la maquina eligio: ", maquina)
        print("punto para el usuario")


    if cont_usuario==3 or cont_maquina==3:
        bandera=False

if cont_usuario==3:
    print("¡felicidades, has ganado!")
else:
    if cont_maquina==3:
        print("¡has perdido!")