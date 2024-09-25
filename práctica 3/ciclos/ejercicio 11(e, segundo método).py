#Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
#muestre en pantalla los primeros c divisores de n.

n=int(input("número n: "))
c=int(input("número c: "))
cont=c
i=1

while cont>0 and i<n:
    if n%i==0:
        print(i, end=" ")
        cont-=1
    i+=1