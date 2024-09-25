#1.hacer una función que dados dos parametros, devuelva el primero elevado al segundo.

#2.hacer una función que tome dos cadenas y devuelva la segunda concatenada con la primera.

#3.hacer una función que dada una cadena, me devuelva la cadena invertida.

def Elevado (n1, n2):
    potencia=n1**n2
    return potencia

def Cadenas(cad1, cad2):
    con=cad2+" "+cad1
    return con

def Invertido (cadena):
    cadnew=""
    for char in cadena:
        cadnew=char+cadnew
    return cadnew

#1.
n=int(input("ingrese un n: "))
m=int(input("ingrese un m: "))
print(Elevado(n,m))

#2.
cad1=input("palabra: ")
cad2=input("palabra: ")
print(Cadenas(cad1, cad2))

#3.
pal=input("palabra: ")
print(Invertido(pal))