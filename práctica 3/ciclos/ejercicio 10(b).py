#Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
#potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
#16 32.


n=int(input("ingrese un valor positivo para n: "))

while n<0:
    n=int(input("el valor ingresado es negativo, intentelo de nuevo: "))

i=0

while i<n:
    potencia=2**i
    i=i+1
    print(potencia, end=" ")