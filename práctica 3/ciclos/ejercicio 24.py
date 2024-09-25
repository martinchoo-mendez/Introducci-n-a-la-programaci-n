#¿Para qué números enteros distintos de cero es cierto que A + B + C = A x B x C ? (lo
#curioso es que sólo hay una solución)

a=int(input("ingrese un valor para a: "))
b=int(input("ingrese un valor para b: "))
c=int(input("ingrese un valor para c: "))

suma=a+b+c
multi=a*b*c

if suma==multi:
    print("los número enteros distintos de cero que su suma es igual a su producto, son:",a,b,c)
else:
    print("a+b+c es distinto de a*b*c")