#Hacer en pseudocodigo y luego un programa que calcule el importe que se le facturará a un
#cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa
#fija de 480 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
#a 25,5 pesos el KW, además se agregan $78 de impuestos. Se leen los valores del medidor al
#comienzo y al fin del período.


kwconsumido=int(input("por favor, ingrese cantidad de kw consumidos: "))
impuesto=78
fijo=480
if kwconsumido<200:
    gasto=fijo+impuesto
else:
    diferencia=kwconsumido-200
    gasto=fijo+impuesto+diferencia*25.5
print("el gasto es: ", gasto)