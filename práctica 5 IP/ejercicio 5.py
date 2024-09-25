#Definir una función llamada sonFactores que tome un entero n y una lista de enteros, y
#devuelva True si los números de la lista son factores de n (es decir, si n es divisible por todos
#ellos).

from funcionesListas import sonFactores

lista=[1,2,5,10]
n=int(input("ingrese un número n: "))
factores=sonFactores(lista,n)
print(factores)