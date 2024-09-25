#Un profesor clasifica las notas de sus alumnos de la siguiente manera:
#1-3 Reprobado
#4-6 Debe rendir examen nal
#7-10 Eximido
#b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasificación
#del mismo.

nota1=int(input("por favor, ingrese primer nota: "))
nota2=int(input("por favor, ingrese segunda nota: "))
nota3=int(input("por favor, ingrese tercer nota: "))
promedio=(nota1+nota2+nota3)/3

if promedio>=1 and promedio<=3:
    print("reprobado")
else:
    if promedio>=4 and promedio<=6:
        print("debe rendir final")
    else:
        if promedio>=7 and promedio<=10:
            print("eximido")