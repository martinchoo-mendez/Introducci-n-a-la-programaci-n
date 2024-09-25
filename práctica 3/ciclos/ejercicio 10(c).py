#Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
#potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
#256. Es decir, 11 22 33 44

n=int(input("ingrese un valor positivo para n: "))

while n<0:
    n=int(input("el valor ingresado es negativo, intentelo de nuevo: "))

i=1
while i<=n:
    potencia=i**i
    i=i+1
    print(potencia, end=" ")