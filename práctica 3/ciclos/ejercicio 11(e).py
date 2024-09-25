#Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
#muestre en pantalla los primeros c divisores de n.

n=int(input("ingrese un valor positivo para n: "))
c=int(input("ingrese un valor positivo para c: "))

while n<0:
    n=int(input("el valor ingresado para n es negativo, intentelo de nuevo: "))

while c<0:
    c=int(input("el valor ingresado para c es negativo, intentelo de nuevo: "))

i=1
cont=0
while cont<c:
    if n%i==0:
        print(i, end=" ")
        cont=cont+1
    i=i+1