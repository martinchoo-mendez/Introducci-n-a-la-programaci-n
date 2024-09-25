#Escribir una función llamada intercambiar que tome una lista de números s y dos enteros
#positivos a y b menores que la longitud de la lista y cambie el elemento ubicado en s[a] por el
#elemento ubicado en s[b]. Ojo, esta función no debe devolver una lista, sino modicar la que
#toma como parámetro.

from funcionesListas import intercambiar

lista=[2,5,4,7,4,1,9]
a=int(input("ingrese un valor para a: "))
b=int(input("ingrese un valor para b: "))
cambio=intercambiar(lista, a, b)
print(cambio)