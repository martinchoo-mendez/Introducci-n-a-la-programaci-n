#Ídem anterior pero deberá frenarse cuando el lado izquierdo pase a ser más grande
#que el derecho.

m=int(input("ingrese un número: "))
n=int(input("ingrese otro número: "))

while m<=n:
    print(m,n)
    m+=1
    n-=1