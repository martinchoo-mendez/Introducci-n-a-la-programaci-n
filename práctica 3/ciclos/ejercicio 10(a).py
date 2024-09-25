#Hacer un programa que reciba un número n y muestre todas las potencias de 2
#menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8
#16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for

n=int(input("ingrese un valor para n: "))

i=0
resultado= 0

while resultado<n:
    potencia=2**i
    i=i+1
    resultado=resultado+potencia
    print(potencia, end=" ")