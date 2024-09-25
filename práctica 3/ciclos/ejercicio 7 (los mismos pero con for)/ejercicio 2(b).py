#Hacer un programa que permita al usuario elegir un número m y un n y luego
#muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¾Qué pasa
#si n es menor que m?

m=int(input("por favor, ingrese un valor m. "))
n=int(input("por favor, ingrese un valor n: "))

for i in range (m, n+1):
    print(i, end=" ")