#Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla todos los divisores de n.

n=int(input("ingrese un valor positivo para n: "))

while n<0:
    n=int(input("el valor ingresado es negativo, intentelo de nuevo: "))

i=1
while i<=n:
    if n%i==0:
        print(i, end=" ")
    i=i+1