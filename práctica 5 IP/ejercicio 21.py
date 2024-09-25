#Definir una función que tome una lista de números s y un número decimal x y cambie todos
#los elementos menores que x por 0.
#Ej:
#Para
#s = [1, 4.1, 6.3, 2, 3.2, 8]
#x = 3
#el la lista debe pasar a ser:
#s = [0, 4.1, 6.3, 0, 3.2, 8]

from funcionesListas import menorAx

s = [1, 4.1, 6.3, 2, 3.2, 8]
x = float(input("ingrese un decimal: "))

cambio=menorAx(s,x)
print(cambio)