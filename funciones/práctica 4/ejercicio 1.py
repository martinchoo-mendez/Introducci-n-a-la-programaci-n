import math

#a) raíz cuadrada de x

x=int(input("ingrese un número: "))

raíz_cua=math.sqrt(x)

print(raíz_cua)

#b) valor absoluto de x

x=int(input("ingrese un número: "))

valor_abs=abs(x)

print(valor_abs)

#c) valor absoluto de x-3

x=int(input("ingrese un número: "))

módulo=abs(x-3)

print(módulo)

#d) raíz cuadrada de módulo de x-5

x=int(input("ingrese un número: "))

calculo=math.sqrt(abs(x-5))

print(calculo)