#Hacer un programa que guarde la siguiente lista en una variable: [elefante, jirafa,
#mono], luego pida el nombre de otro animal, lo agregue a la lista e imprima en pantalla el
#cuarto animal de la lista.

animales=["elefante","jirafa","mono"]

animal=input("ingrese el nombre de otro animal: ")

animales.append(animal)

print(animales[3])