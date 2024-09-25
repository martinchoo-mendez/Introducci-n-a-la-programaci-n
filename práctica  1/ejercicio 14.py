#Una empresa telefónica desea un programa para calcular el importe de sus clientes. Sabiendo que el
#costo por comunicación es de $12 y por cada segundo se cobra $1, 5 hacer dicho programa. Se deben
#ingresar la cantidad de llamadas realizadas y el tiempo total de comunicación, el programa debe devolver
#el precio a cobrar. Por ejemplo, si realizó 10 llamadas con un total de 4000 segundos el importe a pagar
#sería de $6120

costComunicación=12
costSegundo=1.5
cantLlamadas=int(input("por favor, ingrese cantidad de llamadas realizadas: "))
tiempo=int(input("por favor, ingrese cantidad de segundos de llamada: "))

totalSeg=costSegundo*tiempo
totalLlamadas=costComunicación*cantLlamadas
precioFinal=totalSeg+totalLlamadas

print("el importe que debe pagar es: ", precioFinal, "ARS")