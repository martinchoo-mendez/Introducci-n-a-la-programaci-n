#una empresa proveedora de alimentos, necesita generar un código aleatorio por cada producto, según las siguientes reglas:
#-El primer caracter debe ser una vocal aleatoria del nombre del producto en mayúscula.
#-El segundo y tercer caracter deben ser dos consonantes en minúsculas del nombre del producto (no hace falta chequear repetidos).
#-Luego un número entre 0 y 99.
#-El último caracter debe ser un # si la cantidad de caracteres del nombre del producto es par, y en caso contrario, debe ser un *.

#Se nos pide realizar un programa que, dado un nombre de producto, genere su respectivo código. Por ejemplo, si el usuario ingresa
#"tomates triturados", un código posible sería: Etm55#.

import random
producto=input("por favor, ingrese un producto: ")
vocales="aeiouAEIOU"
consonantes="bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
vocalesPalabra=""
consonantesPalabra=""
codigo=""

for letra in producto:
    if letra in consonantes:
        consonantesPalabra += letra
    if letra in vocales:
        vocalesPalabra += letra

codigo += random.choice(vocalesPalabra).upper()

cont=0
for letra in consonantesPalabra:
    if cont<2:
        codigo+=letra.lower()
    cont+=1

numero=random.randint(0,100)
codigo+=str(numero)

cantCaracteres=len(producto)
if cantCaracteres%2==0:
    codigo+="#"
else:
    codigo+="*"

print(codigo)