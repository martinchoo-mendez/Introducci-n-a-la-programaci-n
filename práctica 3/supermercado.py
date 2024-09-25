producto=input("ingrese producto, FIN para terminar")
precio=int(input("ingrese valor de producto: "))

costoTotal=precio
cant=0

while producto!="FIN":
    producto=input("ingrese producto, FIN para terminar")
    if producto!="FIN":
        precio=int(input("ingrese valor de producto: "))
        cant=cant+1
        costoTotal=costoTotal+precio
        print("lleva gastado $", costoTotal)
    else:
        cant=cant+1
print("usted compró ", cant, "productos")
print("usted gastó $", costoTotal)
print("gracias por comprar en el chino Juan, saludos!")