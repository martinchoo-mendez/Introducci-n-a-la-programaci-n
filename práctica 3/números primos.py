#números primos

#método con while
n=int(input("ingrese número: "))
i=1
cont=0

while i<=n:
    if n%i==0:
        cont=cont+1
    i=i+1
print("el número", n, "tiene", cont, "divisores")

if cont==2:
    print("el número ", n, "es primo")
else:
    print("el número ", n, "no es primo")

#método con for
n=int(input("ingrese un número: "))
cont=0

for i in range (1, n+1):
    if n%i==0:
        cont=cont+1
print("el número ", n, "tiene ", cont, "divisores")

if cont==2:
    print("el número ", n, "es primo")
else:
    print("el número ", n, "no es primo")