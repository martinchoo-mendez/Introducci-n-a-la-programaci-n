#Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
#ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
#verificar los resutlados.

n1=int(input("por favor, ingrese un número: "))
n2=int(input("por favor, ingrese otro número: "))
n3=int(input("por favor, ingrese otro número: "))

if n1>n2 and n1>n3:
    print("el mayor es: ", n1)
else:
    if n2>n1 and n2>n3:
        print("el mayor es: ", n2)
    else:
        print("el mayor es: ", n3)