#Hacer un programa que permita al usuario elegir un número m, un n y un p y
#luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
#ejemplo, si el usuario ingresara un m igual a 2 y un n igual a 14, y un p igual a 4,
#el programa deberá mostrar 2, 6, 10, 14

m=int(input("por favor, ingrese un valor m: "))
n=int(input("por favor, ingrese un valor n: "))
p=int(input("por favor, ingrese un valor p: "))

for i in range (m,n+1,p):
    print(i, end= " ")