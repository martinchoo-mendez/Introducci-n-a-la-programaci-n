#Definir una función que tome un entero n y devuelva los primeros n primos.

from funcionesListas import *

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
##def EnterosPrimos(n):
##    lista=[]
##    i=1
##    while i<=n:
##        if i==Primos(i):
##            lista.append(i)
##        i=i+1
##    return lista
#programa principal

n=int(input("número: "))
print(EnterosPrimos(n))