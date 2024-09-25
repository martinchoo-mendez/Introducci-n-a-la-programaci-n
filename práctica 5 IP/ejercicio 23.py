#Modificar el programa del ejercicio 1.2 para que muestre visualmente los resultados, repitiendo
#asteriscos. Ej:
#Palabra ingresada: "conocido"
#c : **
#o : ***
#n : *
#i : *
#d : *

pal=input("ingrese una palabra: ")
revisadas=""

for char in pal:
    cont=0
    if char not in revisadas:
        for letra in pal:
            if char==letra:
                cont+=1
        revisadas=revisadas+char
        print(char, ":", cont*"*")