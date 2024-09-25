#dada una cadena del usuario, generar otra con el primer y último caracter de la original.
nombre=input("ingrese su nombre: ")
cadenanew=""
c=1

for char in nombre:
    if c==1 or c==len(nombre):
        cadenanew=cadenanew+char
    c=c+1
print(cadenanew)