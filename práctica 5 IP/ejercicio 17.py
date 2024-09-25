#Definir una función llamada mcd que tome dos enteros positivos y devuelva el máximo común
#divisor usando funciones de los ejercicios anteriores.

#def multiplo (n):
#    lista_multiplo=[]
#    i=1
#    while i<=n:
#        if n%i==0:
#            lista_multiplo.append(i)
#        i+=1
#    return lista_multiplo
#
#def últimoelemento (lista):
#    ultimo=len(lista)-1
#    return lista[ultimo]
#
#def multiplos_común (m, n):
#    multiplo_n=multiplo(n)
#    multiplo_m=multiplo(m)
#    lista_multiplos=[]
#    for i in range(len(multiplo_n)):
#        for j in range(len(multiplo_m)):
#            if multiplo_n[i]==multiplo_m[j]:
#                lista_multiplos.append(multiplo_n[i])
#    mcd=últimoelemento(lista_multiplos)
#    return mcd

from funcionesListas import multiplos_común

n=int(input("ingrese un número: "))
m=int(input("ingrese un segundo número: "))
mcd=multiplos_común(n, m)
print(mcd)