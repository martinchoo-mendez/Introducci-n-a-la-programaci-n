#a)Definir una función que tome una lista de números s y un número decimal x y
#devuelva la cantidad de elementos de s que sean menores que x.

from funcionesListas import cantMenorAX

s = [1, 4.1, 6.3, 2, 3.2, 8]
x = float(input("ingrese un decimal: "))

cantMenores=cantMenorAX(s,x)
print("los menores a",int(x),"son",cantMenores)