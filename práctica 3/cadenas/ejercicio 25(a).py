#Escribir un programa que pida al usuario un número n y muestre una línea de n
#asteriscos. Ejemplo, para n = 8, el programa deberá mostrar:
#********

n=int(input("por favor, ingrese un número: "))
i=1

#método con while
while i<=n:
    print("*", end="")
    i=i+1
print("FIN")

#método con for
for i in range (1, n+1):
    print("*", end="")