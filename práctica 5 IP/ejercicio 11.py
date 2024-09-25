#Escribir una función llamada maximoEntre que tome una lista de números y dos enteros a y b
#menores que la longitud de la lista y devuelva el índice del máximo elemento considerando solo
#los que están entre el índice a y el índice b.

from funcionesListas import máximoEntre

lista=[2,5,4,7,4,1,9]
a=int(input("ingrese un valor"))
b=int(input("ingrese otro valor"))

mayorEntre=máximoEntre(lista, a, b)
print(mayorEntre)