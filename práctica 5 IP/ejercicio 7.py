#Definir una función llamada dondeAparece que tome una lista de enteros y un entero llamado
#blanco como parámetros, y devuelva el primer índice donde blanco aparece en el arreglo, si lo
#hace, y -1 en caso contrario.

from funcionesListas import dondeAparece

lista=[1,2,3,4,5,6,7,8,9]
blanco=int(input("ingrese un número: "))
aparece=dondeAparece(lista, blanco)
print(aparece)