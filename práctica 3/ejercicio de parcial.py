#Dadas dos cadenas de caracteres  (cadena1 y cadena2), hacer un programa que arme
#una nueva cadena tal que los primeros caracteres sean los de posiciones impares de
#cadena1 y los últimos de posiciones pares de cadena2.
#Por ejemplo: cadena1=“hola” y cadena2=“leones” debe armar la nueva cadena “hlens”.
#(los dos primeros caracteres son el primero y el tercero de cadena1 y los tres últimos
#el segundo, el cuarto y el sexto  de cadena2).

cadena1=input("ingrese una palabra: ")
cadena2=input("ingrese una palabra: ")
cadena=""

c=1
for char in cadena1:
    if c%2!=0:
        cadena=cadena+char
    c=c+1
#print(cadena)

c=1
for letra in cadena2:
    if c%2==0:
        cadena=cadena+letra
    c=c+1
print(cadena)