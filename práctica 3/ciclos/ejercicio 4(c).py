#Hacer un programa que permita al usuario elegir un número n, un m y un p y
#luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
#ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
#el programa deberá mostrar 2, 6, 10, 14.

n=int(input("por favor, ingrese un valor n: "))
m=int(input("por favor, ingrese un valor m "))
p=int(input("por favor, ingrese un valor p: "))

while n<=m:
    print(n, end= " ")
    n=n+p