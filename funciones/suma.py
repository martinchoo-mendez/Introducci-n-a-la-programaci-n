#función que sume dos valores

def Suma (v1, v2):
    suma=v1+v2
    return suma

#p principal

n=int(input("ingrese un n: "))
m=int(input("ingrese un m: "))

print(Suma(n,m))