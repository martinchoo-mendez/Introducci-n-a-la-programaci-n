#Hacer un programa que permita al usuario elegir un número m y un n y muestre
#pares de numeros complementarios, o sea (m, n)(m + 1, n − 1)(m + 2, n − 2). . .(n −
#1, m + 1)(n, m). Por ejemplo, el usuario ingresa 5 y 10, 5 será el complementario de
#10, 6 el de 9 y 7 el de 8, y deberá mostrarse:
#5 10
#6 9
#7 8
#8 7
#9 6
#10 5

m=int(input("ingrese un número: "))
n=int(input("ingrese otro número: "))
v1=m
v2=n

while m<=v2:
    print(m,n)
    m+=1
    n-=1