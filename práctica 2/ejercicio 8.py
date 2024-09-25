#Escribir en papel un programa que tome un número entero positivo ingresado por el usuario
#y muestre por pantalla Usted ingresó un número de una sola cifra o Usted ingresó un número
#de más de una cifra según corresponda. Realizar 4 corridas de escritorio, escribirlo en Python
#y luego correrlo en la computadora con los valores iniciales de las corridas y verifcar que hayan
#dado como se esperaba.

número=int(input("por favor, ingrese un número: "))
if número<10 and número>-10:
    print("usted ingresó un número de una sola cifra")
else:
    print("usted ingresó un número de más de una cifra")