#Se tiene la siguiente lista con DNIs de personas.
#30612453
#23763290
#21448503
#34582048
#15364857
#Dado otro número de DNI cualquiera, se desea construir un programa que determine si es alguno
#de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python.

dni=int(input("por favor, ingrese su dni: "))
dni1=30612453
dni2=23763290
dni3=21448503
dni4=34582048
dni5=15364857

if dni==dni1 or dni==dni2 or dni==dni3 or dni==dni4 or dni==dni5:
    print("su dni se encuentra en la lista")
else:
    print("su dni no se encuentra en la lista")