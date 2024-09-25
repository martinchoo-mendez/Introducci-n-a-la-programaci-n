#función que me diga si un número es par o impar.

def Espar (n):
    if n%2==0:
        return "Par"
    else:
        return "Impar"

#p principal

valor=int(input("ingrese un valor: "))
print(Espar(valor))