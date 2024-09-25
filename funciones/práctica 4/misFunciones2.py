#3)función que imprime tres veces una cadena
def tres_veces (cad):
    i=1
    while i<=3:
        print(cad)
        i+=1

#4)a.función que muestra promedio de dos números
def promedio (v1,v2):
    promedio=(v1+v2)/2
    return promedio

#4)c.función que muestra promedio de tres números
def promedio_de3 (v1,v2,v3):
    promedio=(v1+v2+v3)/3
    return promedio

#5)función que muestra valor absoluto de un número
def valor_abs (x):
    signo=-1
    if x<0:
        valor=x*signo
    else:
        valor=x
    return valor

#6)a.función que muestra una cadena entre signos de exclamación
def exclamar (unaCadena):
    cadnew="¡"
    cadnew=cadnew+unaCadena
    cadnew=cadnew+"!"
    return cadnew

#6)b.función que muestra una cadena entre tres signos de exclamación
def gritar (unaCadena):
    cadnew="¡¡"
    cadnew=cadnew+exclamar(unaCadena)
    cadnew=cadnew+"!!"
    return cadnew

#7)a.función que eleve al cubo un número
def elevarAlCubo(x1):
    cubo= x1**3
    return cubo

#8)a.función que tire los divisores
def divisores (n):
    i=1
    cant=0
    while i<=n:
        if n%i==0:
            cant=cant+1
        i=i+1
    return cant

#8)b.función que dice si es primo
def esprimo (n):
    cont=0
    i=1
    while i<=n:
        if n%i==0:
            cont=cont+1
        i=i+1
    if cont==2:
        return "True"
    else:
        return "False"

#9)a.función que reciba dos enteros y retorne el mayor.
def esMayor (n1, n2):
    if n1<n2:
        return n2
    else:
        return n1

#9)b.función que reciba tres enteros y retorne el mayor
def esMayor2 (n1, n2, n3):
    if n2<n1 and n3<n1:
        return n1
    elif n1<n2 and n3<n2:
        return n2
    else:
        return n3

#11)a.función que sume los divisores propios de un número
def suma_div (v1):
    suma=0
    i=1
    while i<v1:
        if v1%i==0:
            suma=suma+i
        i=i+1
    return suma

#11)b.función que indica si un número es perfecto
def esPerfecto (v1):
    suma=0
    i=1
    while i<v1:
        if v1%i==0:
            suma=suma+i
        i=i+1
    if suma==v1:
        return "Es Perfecto"
    else:
        return "No Es Perfecto"

#11)c.función que me dice si un número es abundante
def abundante (x):
    suma=0
    i=1
    while i<x:
        if x%i==0:
            suma=suma+i
        i=i+1
    if suma>x:
        return "Es Abundante"
    else:
        return "No Es Abundante"

#14)función que dado un n, devuelve el primer primo mayor
def Primos (n):
    i=1
    cont=0
    while i<=n:
        if n%i==0:
            cont+=1
        i=i+1
    if cont==2:
        return n

def PrimoMayor(n):
    i=n+1
    while i>n:
        if i==Primos(i):
            return i
        i=i+1

#17)a.función que devuelve True si una cadena tiene letras repetidas, o False en caso contrario.
def tieneRepetidas (cadena):
    for char in cadena:
        cont=0
        for letra in cadena:
            if char==letra:
                cont+=1
                if cont==2:
                    return True
    return False

#17)b.función que tome letra y palabra e indique si esa letra aparece en la palabra
def aparece (letra, palabra):
   if letra in palabra:
        return True
   else:
        return False

#17)c.función que devuelve la primer letra que se repita en una palabra.
def dameRepetida (cadena):
    for char in cadena:
        cont=0
        for letra in cadena:
            if char==letra:
                cont+=1
                if cont==2:
                    return char
    return "No tiene repetida"