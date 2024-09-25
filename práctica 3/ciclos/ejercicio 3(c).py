#Hacer un programa que permita al usuario elegir un número n y un número c, y
#luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).

n=int(input("por favor, ingrese un valor n: "))
c=int(input("por favor, ingrese un valor c: "))
i=1

while i<=c:
    print(n+1, end= " ")
    n=n+1
    i=i+1