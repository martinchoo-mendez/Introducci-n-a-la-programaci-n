##Hacer un programa que reciba un número m y determine el primer n para el cual la suma
##1+2+...+n > m. Por ejemplo, si el usuario ingresa 11 se deberá retornar 5 ya que 1+2+3+4 =
##10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11

m=int(input("ingrese un número m: "))

flag=True
suma=0
i=1

while flag:
    suma+=i
    if suma>m:
        flag= False
        i-=1
    i+=1
print(i)

##while suma<m:
##    suma+=i
##    i+=1
##print(i)