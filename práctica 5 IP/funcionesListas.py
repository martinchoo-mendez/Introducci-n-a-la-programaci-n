#2)función que toma una lista de enteros y los muestra separados por espacios.
def mostrarEnUnaLinea ():
    enteros=[1,2,3,4,5,6,7,8,9,10]
    for elem in enteros:
        print(elem,end=" ")

#3)función que toma un entero y devuelva la lista de divisores de ese entero.
def divisores (n):
    i=1
    lista_div=[]
    while i<=n:
        if n%i==0:
            lista_div.append(i)
        i+=1
    return lista_div

#4)función que toma dos listas y devuelva la que menos elementos tiene.
def laMasCorta (l1, l2):
    if len(l1)<len(l2):
        return l1
    elif len(l2)<len(l1):
        return l2
    else:
        return l1

#5)función que tome un entero y una lista de enteros y devuelva True si todos los números de la
#son divisibles por ese entero.
def sonFactores (lista, entero):
    cont=0
    for elem in lista:
        if entero%elem==0:
            cont=cont+1
    print(cont)
    if cont==len(lista):
        return True
    else:
        return False

#6)función que retorne True si tiene, al menos, un repetido, y False en caso contrario.
def aparece (lis1, lis2):
    lista3=[]
    for elem in lis1:
        if elem in lis2:
            lista3.append(elem)
    if len(lista3)>=1:
        return True
    else:
        return False

#7)función que tome una una lista de enteros, y un blanco como parámetros, y devuelva el indice donde blanco aparece en la lista
#y -1 si no lo hace.
def dondeAparece (lis, blanco):
    for i in lis:
        if i==blanco:
            indice=lis.index(i)
            return indice
    else:
        return "-1"

#segundo método
def dondeAparece2 (Lista, blanco):
    for i in range (len(Lista)):
        if Lista[i]==blanco:
            return i
    return -1

#8)función que toma una lista de decimales, y devuelve su promedio de los elementos.
def promDecimales (decimales):
    suma=0
    for i in decimales:
        suma=suma+i
    promedio=suma/len(decimales)
    return promedio

#9)función que devuelve el máximo de una lista de enteros.
def máximo (lista):
    mayor=lista[0]
    for i in range(len(lista)):
        if mayor<lista[i]:
            mayor=lista[i]
    return mayor

#10)función que retorne el indice del mayor elemento
def máximoIndice (lista):
    for i in lista:
        if i==max(lista):
            indice=lista.index(i)
            return indice

#11) que toma una lista de enteros y dos enteros menores a la longitud de la cadena.
#y devuelve el máximo entre esos enteros.
def máximoEntre (lista, a, b):
    lista2=[]
    for i in lista:
        if lista.index(i)>=a and lista.index(i)<=b:
            lista2.append(i)
    for j in lista2:
        if j==max(lista2):
            return j

#12)función que intercambia los elementos que están en la posición a y en la posición b,
def intercambiar (lista, a, b):
    aux=lista[a]
    lista[a]=lista[b]
    lista[b]=aux
    return lista

#13)función que tome una lista s y un entero n, y devuelva la cantidad de veces que n está en s.
def frecuencia (s, n):
    cont=0
    for i in s:
        if i==n:
            cont+=1
    return cont

#14)función que tome dos listas sin elementos repetidos, y devuelva otra con los elementos
#que hay en ambas listas.

#primer método
def intersección (lista1, lista2):
    lista3=[]
    for i in lista1:
        if i in lista2:
            lista3.append(i)
    return lista3

#segundo método
def intersección2 (lista1, lista2):
    lista3=[]
    for i in lista1:
        for j in lista2:
            if i==j:
                lista3.append(i)
    return lista3

#15)función que una dos listas en una nueva, pero, que no tenga repetidos.
def unión (lista1, lista2):
    lista3=lista1+lista2
    unicos=[]
    lista3_copia=list(lista3)
    for i in lista3_copia:
        if i not in unicos:
            unicos.append(i)
        else:
            lista3.remove(i)
    return lista3

#16)función que tome dos listas y devuelva una nueva con los elementos de la primera, que no
#estén en la segunda.

def diferencia(lista1, lista2):
    lista3=[]
    for i in lista1:
        if i not in lista2:
            lista3.append(i)
    return lista3

#17)función que toma dos enteros y devuelve el máximo común divisor.
def multiplo (n):
    lista_multiplo=[]
    i=1
    while i<=n:
        if n%i==0:
            lista_multiplo.append(i)
        i+=1
    return lista_multiplo

def últimoelemento (lista):
    ultimo=len(lista)-1
    return lista[ultimo]

def multiplos_común (m, n):
    multiplo_n=multiplo(n)
    multiplo_m=multiplo(m)
    lista_multiplos=[]
    for i in range(len(multiplo_n)):
        for j in range(len(multiplo_m)):
            if multiplo_n[i]==multiplo_m[j]:
                lista_multiplos.append(multiplo_n[i])
    mcd=últimoelemento(lista_multiplos)
    return mcd

#18)función que devuelve los primos hasta n.
def Primos (n):
    i=1
    cont=0
    while i<=n:
        if n%i==0:
            cont+=1
        i=i+1
    if cont==2:
        return n

def EnterosPrimos(n):
    lista=[]
    i=1
    while i<=n:
        if i==Primos(i):
            lista.append(i)
        i=i+1
    return lista

#19)función que tome un n y devuelva los primos que factorean n.
def primo (n):
    cont=0
    i=1
    while i<=n:
        if n%i==0:
            cont+=1
        i+=1
    if cont==2:
        return n

def factoreo (n):
    lista=[]
    i=1
    bandera=True
    while bandera:
        if primo(i):
            if n%i==0:
                lista.append(i)
                n=n/i
            else:
                i+=1
                if i>n:
                    bandera=False
        else:
            i+=1
    return lista

#20)a.función que toma una lista y un x decimal, y devuelva la cantidad de elementos menores
#a x que hay en la lista.
def cantMenorAX (lista, x):
    cont=0
    for i in range(len(lista)):
        if lista[i]<x:
            cont+=1
    return cont

#21)función que toma una lista y un x decimal, y cambia los elementos menores a x, por 0.
def menorAx (lista, x):
    for i in range(len(lista)):
        if lista[i]<x:
            lista[i]=0
    return lista