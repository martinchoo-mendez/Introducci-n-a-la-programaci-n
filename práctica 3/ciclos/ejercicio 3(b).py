#Hacer un programa que permita al usuario elegir un número n y luego muestre los
#5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).

n=int(input("por favor, ingrese un número: "))
i=1

while i<=5:
    print(n+1, end=" ")
    n=n+1
    i=i+1
