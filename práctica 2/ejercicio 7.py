#Escribir en papel un programa que pida al usuario dos números de punto flotante y muestre
#su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
#"Aprobado" y si no, debe mostrar "Desaprobado". Después de hacerlo en papel, pasarlo a Python.

nota1=float(input("por favor, ingrese una nota: "))
nota2=float(input("por favor, ingrese otra nota: "))
promedio=(nota1 + nota2)/2

if promedio>=7:
    print("aprobado")
else:
    print("desaprobado")