#el número un cuarto de pi.

#Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
#que muestre la aproximación de π con esa cantidad de términos.

n=int(input("ingrese un número: "))
i=1
signo=1
cont=1
serie=0
while cont<=n:
    serie=serie+(1/i)*signo
    i=i+2
    signo=signo*(-1)
    cont=cont+1
print(serie)