#Hacer un programa que genere una clave provisoria para la gestión online de clientes de una
#empresa. El programa le pedirá el apellido y generará una clave de 5 caracteres, tomará las
#primeras 4 consonantes de la palabra ingresada. Cuando las consonantes no alcancen a 4, las
#faltantes las reemplazará por "*". Ejemplos:
#clemente CLMN
#rivera RVR*
#oreo R***
#La clave se completará con 1 dígito generado aleatoriamente entre 0 y 9.
#Ejemplos: CLMN1 RVR*4 R***7

apellido=input("ingrese su apellido: ")
consonantes="bcdfghjklmnpqrstvwxyz"
clave=""

c=1
for char in apellido:
    if char in consonantes:
        if c==1 or c==2 or c==3 or c==4:
            clave=clave+char
        c=c+1
#print(clave)

while len(clave)<4:
    clave=clave+"*"
#print(clave)

import random
azar=random.randint(0,9)
clave=clave+str(azar)
print(clave)