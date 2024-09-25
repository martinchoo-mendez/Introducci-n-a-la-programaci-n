#Hacer un programa que dada una palabra y una letra, imprima la cantidad de apariciones de
#esa letra.

palabra=input("por favor, ingrese una palabra: ")
letra=input("ingrese una letra: ")
cont=0

for char in palabra:
    if char==letra:
        cont+=1

if cont==0:
    print("la letra", letra, "no aparece en la palabra ingresada.")
elif cont==1:
    print("la letra", letra, "aparece", cont, "vez.")
else:
    print("la letra", letra ,"aparece", cont, "veces.")