#Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla las n primeras sumas parciales de la sucesión an=n**3-n**2

n=int(input("ingrese un valor positivo para N: "))

while n<0:
    n=int(input("ingrese un valor positivo para N: "))

i=1
suma=0
while i<=n:
    sucesión=i**3-i**2
    i=i+1
    suma=suma+sucesión
    #print(sucesión, end=" ")
    print(suma, end=" ")