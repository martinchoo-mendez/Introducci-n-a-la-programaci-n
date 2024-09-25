#Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
#muestre en pantalla los últimos c divisores de n.

n=int(input("número n: "))
c=int(input("número c: "))
i=n
cont=c

while i<=n and i>0 and cont>0:
    if n%i==0:
        print(i, end=" ")
        cont-=1
    i-=1