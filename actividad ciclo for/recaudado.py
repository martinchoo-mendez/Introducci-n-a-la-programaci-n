recaudado=0
for i in range (1,10+1):
    cuanto=int(input("¿cuánto pondrá?\nmonto: "))
    recaudado=cuanto+recaudado
    print("estamos por $", recaudado)
print("se recaudó $", recaudado)