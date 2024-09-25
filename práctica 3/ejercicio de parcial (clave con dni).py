#se solicita el dni
#se crea una clave temporal con su dni, de la siguiente manera:
#1.se toman los dos primeros valores del dni
#2.se suman ese par de números, y si el valor es menor a 10, se repite ese valor;y si es mayor, se conserva
#3.la clave será la combinación obtenida, pero al revés.

dni=input("ingrese su dni: ")
combinación=""
clave=""
pridig=""
segdig=""

c=1
for dni1 in dni:
    if c==1:
        pridig=pridig+dni1
    c=c+1

c=1
for dni2 in dni:
    if c==2:
        segdig=segdig+dni2
    c=c+1

combinación=combinación+pridig+segdig

#print(combinación)

suma=int(pridig)+int(segdig)
if suma<10:
    combinación=combinación+str(suma)+str(suma)
else:
    combinación=combinación+str(suma)

#print(combinación)

for char in combinación:
    clave=char+clave
print("su claves es ", clave)