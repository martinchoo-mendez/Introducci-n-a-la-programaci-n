#Hacer un programa que solicite dos cadenas, nombre y apellido y arme el legajo de estudiantes
#de la universidad de la siguiente manera:
#Los 3 primeros números del legajo coinciden con los primeros del dni luego "_", luego las 3
#primeras letras del apellido y por ultimo la primera y ultima del nombre.
#Por ejemplo:
#JavierRodriguez 38946702
#Legajo: 389_rodjr

nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
dni=input("ingrese su dni: ")
legajo=""
c=1

for dni1 in dni:
    if c==1 or c==2 or c==3:
        legajo=legajo+dni1
    c=c+1
legajo=legajo+"_"
#print(legajo)

c=1
for letra in apellido:
    if c==1 or c==2 or c==3:
        legajo=legajo+letra
    c=c+1
#print(legajo)

c=1
for char in nombre:
    if c==1 or c==len(nombre):
        legajo=legajo+char
    c=c+1
print(legajo)