#Suponga que una persona desea invertir su capital en un banco y quiere saber cuánto dinero tendrá en
#su cuenta si el banco incrementa el 6 % mensual(no acumulativo). Se le debe pedir al usuario el capital
#a invertir y la cantidad de meses. Por ejemplo, si invierte 500 mil pesos por 4 meses el banco debería
#devolverle 620 mil pesos.

capital=int(input("por favor, ingrese capital a invertir: "))
meses=int(input("por favor, ingrese la cantidad de meses: "))

intereses=capital*meses*(6/100)
total=capital+intereses

print("al finalizar los ",meses, "meses, usted tendrá: ", total, "ARS")