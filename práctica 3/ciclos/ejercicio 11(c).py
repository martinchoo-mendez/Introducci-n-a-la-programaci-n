#Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla la cantidad de divisores de n.

n=int(input("ingrese un valor positivo para n: "))

while n<0:
    n=int(input("el valor ingresado es negativo, intentelo de nuevo: "))

i=1
cont=0

while i<=n:
    if n%i==0:
        cont=cont+1
    i=i+1
print(cont)