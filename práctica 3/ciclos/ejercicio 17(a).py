##El número 1/4π se puede aproximar de la siguiente manera:
##1/4π = 1 − 1/3 + 1/5 − 1/7 + 1/9 − 1/11 + 1/13 − 1/15

##Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
##que muestre la aproximación de π con esa cantidad de términos.

n=int(input("ingrese un número: "))

i=1
numerador=1
denominador=1
suma=0
signo=1

while i<=n:
    serie=(numerador/denominador)*signo
    i+=1
    denominador+=2
    suma+=serie
    signo*=-1
print(suma)