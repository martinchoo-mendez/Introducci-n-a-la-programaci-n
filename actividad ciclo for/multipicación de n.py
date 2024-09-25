#Realizar un programa que imprima la tabla del número que el usuario
#desee (desde el 1 al 10). Hacer ahora una versión con ciclos for.

#metodo con for:
n=int(input("por favor, ingrese un valor n: "))
for i in range (1, 10+1):
    multi=n*i
    print(n, "x", i, "es= ", multi)

#metodo con while
n=int(input("por favor, ingrese un valor n: "))
i=1
while i<=10:
    multi=n*i
    print(n, "x", i, "es=", multi)
    i=i+1