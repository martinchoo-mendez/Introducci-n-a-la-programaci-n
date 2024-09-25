#Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
#que muestre la aproximación de ln(2) con esa cantidad de términos.

n=int(input("cantidad de términos\n"))

i=1
signo=-1
suma=0

while i<=n:
    logaritmo2=-1/i *signo
    suma=suma+logaritmo2
    i=i+1
    signo=signo*(-1)
print(suma)