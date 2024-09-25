#Escribir un programa que pida al usuario una cadena y una letra y reemplace las apariciones
#de dicha letra por asteriscos. Por ejemplo, si el usuario ingresa:
#"programador"
#"r"
#el programa debe devolver "p ∗ og ∗ amado∗"

cadena=input("por favor, ingrese una palabra: ")
letra=input("por favor, elija una letra: ")
cadenanew=""

for char in cadena:
    if char!=letra:
        cadenanew=cadenanew+char
    else:
        cadenanew=cadenanew+"*"
print(cadenanew)