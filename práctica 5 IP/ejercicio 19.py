#Definir una función que tome un entero n y devuelva la lista de los primos que aparecen al
#factorear n. Ejemplo, para 24, la lista debe ser: [2, 2, 2, 3]

#def primo (n):
#    cont=0
#    i=1
#    while i<=n:
#        if n%i==0:
#            cont+=1
#        i+=1
#    if cont==2:
#        return n

#def factoreo (n):
#    lista=[]
#    i=1
#    bandera=True
#    while bandera:
#        if primo(i):
#            if n%i==0:
#                lista.append(i)
#                n=n/i
#            else:
#                i+=1
#                if i>n:
#                    bandera=False
#        else:
#            i+=1
#    return lista

from funcionesListas import factoreo

n=int(input("ingrese un número: "))
factores=factoreo(n)
print(factores)