#Problema, se cuenta con:
#   .Un intervalo numérico [n, m] donde n es menor a m.
#   .Un número natural denominado d, que pertenece al intervalo [n,m]
#Realizar un programa en Python donde:
#Un usuario ingrese: los valores n, m correspondiente a dicho intervalo, asumiendo que n<m.
#El usuario ingresa además, el valor de d asumiendo que pertenece al intervalo [1, n].
#Realizar un proceso que debe mostrar todos los múltiplos de d, en el intervalo [n, m]
#Por ejemplo (son solos ejemplos, el programa debe funcionar para cualquier juego de datos
#conforme al enunciado):
#-n=40  m=100  d=5
#   los valores que se muestra son: 40, 45, 50, 55, 60, 65....100.
#-n=8  m=13  d=7
#   no se muestra nada, porque 7 no tiene multiplos entre 8 y 13.

n=int(input("ingrese un valor n: "))
m=int(input("ingrese un valor m: "))
d=int(input("ingrese un valor d: "))

while n<=m:
    if n%d==0:
        print(n, end=" ")
    n+=1

#si tuvieramos que mostrar la cantidad de multiplos?
n=int(input("ingrese un valor n: "))
m=int(input("ingrese un valor m: "))
d=int(input("ingrese un valor d: "))
cont=0
while n<=m:
    if n%d==0:
       cont+=1
    n+=1
print(cont)

#si tuvieramos que mostrar la suma de los multiplos?
n=int(input("ingrese un valor n: "))
m=int(input("ingrese un valor m: "))
d=int(input("ingrese un valor d: "))
suma=0
while n<=m:
    if n%d==0:
        suma=suma+n
    n+=1
print(suma)