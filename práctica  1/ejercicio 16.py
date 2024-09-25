#Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
#El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
#b el intermedio y en c el mayor (es decir, ordenará los valores).

a=int(input("por favor, ingrese un valor a: "))
b=int(input("por favor, ingrese un valor b: "))
c=int(input("por favor, ingrese un valor c: "))

if a<b and a<c:
    print(a)
else:
    if b<a and b<c and a<c:
        aux=a
        a=b
        b=c
        c=aux
        print(a, b, c)