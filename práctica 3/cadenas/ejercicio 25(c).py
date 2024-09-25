#Escribir un programa que pida al usuario un número n y muestre n líneas de 2n − 1
#asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá mostrar:
#*
#***
#*****
#*******
#*********

#método con while
n=int(input("ingrese un valor n: "))
i=1
ast="*"

while i<=n:
    print(ast)
    i=i+1
    ast=ast+"**"

#método con for
n=int(input("ingrese un valor n: "))
ast="*"
for i in range (1, n+1):
    print(ast)
    ast=ast+"**"