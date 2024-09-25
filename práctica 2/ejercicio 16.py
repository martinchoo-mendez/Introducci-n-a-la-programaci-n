#Un año es bisiesto si es múltiplo de 4. Pero no siempre, las excepciones son los años múltiplos
#de 100 que no son múltiplos de 400 (1900 no es bisiesto pero 2000, sí). Escribir en papel un
#programa que diga si un año ingresado por el usuario es bisiesto, realizar varias pruebas de
#escritorio, luego pasarlo a Python y vericar los resutlados.

año=int(input("por favor, ingrese un año: "))

if año%4==0:
    if año%100==0 and año%400!=0:
        print("el año ingresado no es bisiesto")
    else:
        print("el año ingresado es bisiesto")
else:
    print("el año ingresado no es bisiesto")