#Definir una función llamada diferencia que tome dos listas sin repetidos y devuelva una
#nueva lista que contenga los elementos de la primera que no estén en la segunda.

from funcionesListas import diferencia

lista1=[2,5,4,7,1,3,9]
lista2=[3,6,4,5,1,8,0]

nuevaLista=diferencia(lista1, lista2)
print(nuevaLista)