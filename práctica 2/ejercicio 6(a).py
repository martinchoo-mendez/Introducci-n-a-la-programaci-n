#Escribir en papel un programa que pida al usuario dos números, y que muestre en
#pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a
#Python y por último correr el programa con los valores iniciales de las corridas y
#verificar que funciona como se esperaba

n1=int(input("por favor, ingrese un número : "))
n2=int(input("por favor, ingrese otro número :"))

if n1>n2:
    print("entre estos dos números, el mayor es: ", n1)
else:
    print("entre estos dos números, el mayor es: ", n2)