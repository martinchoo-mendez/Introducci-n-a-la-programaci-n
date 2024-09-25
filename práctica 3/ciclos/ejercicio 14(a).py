#Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla los n primeros términos de la sucesión an = 2n. Es decir 2, 4,
#6..

n=int(input("ingrese un valor positivo para N: "))

while n<0:
    n=int(input("ingrese un valor positivo para N: "))

i=1
while i<=n:
    sucesión=2*i
    i=i+1
    print(sucesión, end=" ")
