#Hacer un programa que indique si un número es abundante.
#Un número es abundante si la suma de los divisores propios supera al mismo número.
#Por ejemplo, 12 es abundante pues los divisores propios son 1 2 3 4 y 6 que suman en total 16 que es mayor a 12.

n=int(input("ingrese un número: "))
i=1
suma=0

while i<n:
    if n%i==0:
        suma=suma+i
    i=i+1
print(suma)

if suma>n:
    print("el número es abundante")
else:
    print("el número no es abundante")