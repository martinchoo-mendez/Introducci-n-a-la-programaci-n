#Escribe un programa que pida los coecientes de una ecuación de primer grado (ax + b = 0)
#y escriba la solución. Recuerda que una ecuación de primer grado puede no tener solución, tener
#una solución única, o que todos los números reales sean solución.

print("este programa calcula ax+b=0")
a=float(input("por favor, ingrese un valor a: "))
b=float(input("por favor, ingrese un valor b: "))

if a==0:
    print("la ecuación tiene infinitas soluciones")
else:
    solución=-b/a
    print("la solución es: ", solución)