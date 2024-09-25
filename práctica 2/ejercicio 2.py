#Un ciudadano argentino está exento de votar en estos casos:
#Tiene más de 70 años
#Tiene entre 18 y 70 años pero se encuentra a más de 500 km del centro de votación.
#Suponiendo que las variables edad y distancia representan la edad y la distancia del ciudadano,
#escribir la expresión lógica que representa esta situación

km=int(input("¿a cuántos km se encuentra del centro de votación? "))

if km<=500:
    edad=int(input("por favor, ingrese su edad: "))
    if edad>18 and edad<70:
        print("usted debe votar")
    else:
        print("usted está excento de votar")
else:
    print("usted está excento de votar")