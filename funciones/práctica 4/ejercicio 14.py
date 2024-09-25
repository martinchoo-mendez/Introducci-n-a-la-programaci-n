##Hacer un programa que solicite al usuario un número entero positivo e indique cuál es el
##número primo mayor más cercano. Usar funciones. Por ejemplo, si el usuario ingresa 24, el
##programa devolverá 29 (29 es el número primo más cercano mayor que 24). Si el usuario ingresa
##5 el programa devolverá 7.

from misFunciones import *

##def Primos (n):
##    i=1
##    cont=0
##    while i<=n:
##        if n%i==0:
##            cont+=1
##        i=i+1
##    if cont==2:
##        return n
##
##def PrimoMayor(n):
##    i=n+1
##    while i>n:
##        if i==Primos(i):
##            return i
##        i=i+1

n=int(input("ingrese un número: "))
mayor=PrimoMayor(n)
print(mayor)