#dada una cadena del usuario, generar otra con el primer y segundo caracter de la original.
nombre=input("ingrese su nombre: ")
cadenanew=""
c=1

for char in nombre:
    if c==1 or c==2:
        cadenanew=cadenanew+char
    c=c+1
print(cadenanew)