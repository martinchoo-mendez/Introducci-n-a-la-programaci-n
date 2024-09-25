#hacer un programa que dada una cadena ingresada, devuelva otra nueva armada únicamente
#por las consonantes. Además, la nueva cadena deberá tener un guión bajo "_" al comienzo
#y al final de la misma.
#ejemplo (tiene que funcionar con cualquier conjunto de palabras):
#"Argentina"
#Nueva cadena: "_rgntn_"

pal=input("ingrese una palabra: ")
consonantes="bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSWTVWXYZ"
cadnew="_"

for char in pal:
    if char in consonantes:
        cadnew=cadnew+char

cadnew=cadnew+"_"

print(cadnew)