#Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre en pantalla
#la cantidad de días, minutos y segundos que representa. Por ejemplo, si el usuario ingresa 86461 segundos
#el programa debe mostrar por pantalla: 1 día 0 horas 1 minuto 1 segundo.

seg=int(input("por favor, ingrese cantidad de segundos a evaluar: "))
segDía=86400
segHora=3600
segMin=60

cantDías=seg//segDía
print(cantDías, "días")
resto=seg%segDía

cantHoras=resto//segHora
print(cantHoras, "horas")
resto2=resto%segHora

cantMin=resto2//segMin
print(cantMin, "minutos")
resto3=resto2%segMin

print(resto3, "segundos")