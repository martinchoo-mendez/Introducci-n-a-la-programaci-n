#Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en
#pantalla el producto (es decir, la multiplicación) de los numeros entre 1 y n

n=int(input("ingrese un valor positivo para N: "))

while n<0:
    n=int(input("ingrese un valor positivo para N: "))

i=1
multi=1
while i<=n:
    multi=multi*i
    i=i+1
    print(multi)