#Hacer una programa que, dada una palabra, la escriba pegada a la derecha de la
#pantalla.

pal=input("ingrese una palabra: ")
longitud=len(pal)
print((" "*(148-len(pal)))+pal)