import math

def calculo(x):
    resultado=math.sqrt(math.log(abs(1-x)))
    return resultado

def Espar (n):
    if n%2==0:
        return "Par"
    else:
        return "Impar"

def Suma (n1, n2):
    suma=n1+n2
    return suma

def Elevado (v1, v2):
    potencia=v1**v2
    return potencia

def Cadenas (cad1, cad2):
    cad=cad2+" "+cad1
    return cad

def Invertido (cadena):
    cadnew=""
    for char in cadena:
        cadnew=char+cadnew
    return cadnew

def mostrarDosVeces(cadena):
    print(cadena)
    print(cadena)

def esPrimo (n):
    cont=0
    bandera=False
    for i in range (1,n+1):
        if n%i==0:
            cont+=1
    if cont==2:
        bandera=True
    return bandera