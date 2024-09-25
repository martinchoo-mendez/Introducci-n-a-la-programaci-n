#Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
#primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
#valores de las variables y mostrarlos de mayor a menor.

n1=int(input("por favor, ingrese un valor 1: "))
n2=int(input("por favor, ingrese un valor 2: "))

if n1<n2:
    aux=n1
    n1=n2
    n2=aux
    print(n1,n2)
else:
    print(n1,n2)