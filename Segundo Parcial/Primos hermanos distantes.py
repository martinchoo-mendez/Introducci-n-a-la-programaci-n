#Desarrollar el programa principal y todas las funciones puras que crea necesarias que soliciten al usuario
#dos números, n y m, y digan si son números primos hermanos distantes.
#Dos números son primos hermanos distantes si ambos son primos y están separados por una distancia de
#cuatro.
#Los números 37 y 41 son primos hermanos distantes, 61 y 67 no lo son.

def EsPrimo (n):
    cont=0
    i=1
    while i<=n:
        if n%i==0:
            cont+=1
        i=i+1
    if cont==2:
        return n

def distancia (n, m):
    diferencia=m-n
    return diferencia

def PrimoHermano (n, m):
    if EsPrimo(n) and EsPrimo(m):
        if distancia(n,m)==4:
            return "Son Primos Hermanos Distantes"
    return "No Son Primos Hermanos Distantes"

n=int(input("ingrese un número: "))
m=int(input("ingrese un segundo número: "))
primo_hermano=PrimoHermano(n, m)
print(n, "y", m, primo_hermano)