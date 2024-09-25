##una función que se llame dameRepetida que tome una cadena como parámetro y
##retorne la primer letra que aparece repetida en la cadena.

from misFunciones import *

##def dameRepetida (cadena):
##    for char in cadena:
##        cont=0
##        for letra in cadena:
##            if char==letra:
##                cont+=1
##                if cont==2:
##                    return char
##    return "No tiene repetida"

cadena=input("ingrese una palabra: ")
letra_repetida=dameRepetida(cadena)
print(letra_repetida)