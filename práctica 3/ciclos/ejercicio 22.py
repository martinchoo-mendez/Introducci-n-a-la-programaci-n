#Hacer un programa que simule el juego de la quiniela. El usuario debe elegir un número del
#0 al 99 y un monto a apostar, si acierta el número gana 70 veces lo apostado. (El número de la
#suerte debe ser elegido al azar)

import random
azar=random.randint(0, 99)
#print(azar)
n=int(input("ingrese un número: "))
monto=int(input("ingrese monto a apostar: "))

if n==azar:
    monto=monto*70
    print("usted ganó ",monto)

else:
    print("usted no ganó")