#listas que se corresponden

def dondeAparece2 (Lista, blanco):
    for i in range (len(Lista)):
        if Lista[i]==blanco:
            return i
    return -1

código=int(input("ingrese el código: "))
ListaCodigos=[1234,345,789]
ListaProductos=["azúcar","yerba","arroz"]
ListadePrecios=[1000,1500,800]

elemento=dondeAparece2(ListaCodigos, código) #busco el indice del código y lo pongo en elemento

if elemento==-1:
    print("Código inexistente")
else:
    print(código)
    print(ListaProductos[elemento]) #me fijo en la lista de productos, el del indice elemento
    print("$",ListadePrecios[elemento]) #me fijo en la lista de productos, el del indice elemento