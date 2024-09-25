#Un profesor clasifica las notas de sus alumnos de la siguiente manera:
#1-3 Reprobado
#4-6 Debe rendir examen final
#7-10 Eximido
#a) Escribir un programa que indique la clasificación de una nota.

nota=int(input("por favor, ingrese una nota: "))
if nota>=1 and nota<=3:
    print("reprobado")
else:
    if nota>=4 and nota<=6:
        print("debe rendir exámen final")
    else:
        if nota>=7 and nota<=10:
            print("eximido")