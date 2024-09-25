##una función que se llame tieneRepetidas que tome una cadena como parámetro y
##devuelva True si esa cadena tiene alguna letra que aparece más de una vez y False
##en caso contrario.

from misFunciones2 import *

##def tieneRepetidas (cadena):
##    for char in cadena:
##        cont=0
##        for letra in cadena:
##            if char==letra:
##                cont+=1
##                if cont==2:
##                    return True
##    return False

palabra=input("ingrese una palabra: ")
repetidas=tieneRepetidas(palabra)
print(repetidas)