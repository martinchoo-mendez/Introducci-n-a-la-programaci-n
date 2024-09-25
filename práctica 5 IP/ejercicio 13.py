#Escribir una función llamada frecuencia que tome una lista de enteros s y otro entero n como
#parametros y devuelva la cantidad de veces que aparece n en s.

from funcionesListas import frecuencia

lista=[5,2,6,9,5,2,7,9,5]
n=int(input("ingrese un valor para n: "))
aparece=frecuencia(lista,n)
print(aparece)