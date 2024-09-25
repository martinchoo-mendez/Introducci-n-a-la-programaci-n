##Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
##El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
##b el intermedio y en c el mayor (es decir, ordenará los valores).

a=int(input("ingrese un número: "))
b=int(input("ingrese otro número: "))
c=int(input("ingrese otro número: "))
menor=0
medio=0
mayor=0

if b<a and b<c and a<c:
    menor=b
    medio=a
    mayor=c
else:
    if b<a and b<c and c<a:
        menor=b
        medio=c
        mayor=a
    else:
        if a<b and a<c and c<b:
            menor=a
            medio=c
            mayor=b
        else:
            if a<b and a<c and b<c:
                menor=a
                medio=b
                mayor=c
            else:
                if c<a and c<b and a<b:
                    menor=c
                    medio=a
                    mayor=b
                else:
                    if c<a and c<b and b<a:
                        menor=c
                        medio=b
                        mayor=a

a=menor
b=medio
c=mayor

print(a, b, c)