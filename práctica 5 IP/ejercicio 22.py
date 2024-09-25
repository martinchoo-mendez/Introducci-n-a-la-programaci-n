#Escribir un programa que pida al usuario una cadena, y luego escriba en pantalla la cantidad
#de veces que aparece cada letra (sin mostrar las que no aparecen). Ej:
#Palabra ingresada: "conocido"
#c : 2
#o : 3
#n : 1
#i : 1
#d : 1

pal=input("ingrese una palabra: ")
revisadas=""

for char in pal:
    cont=0
    if char not in revisadas:
        for letra in pal:
            if char==letra:
                cont+=1
        revisadas=revisadas+char
        print(char, ":", cont)