#La empresa que administra los cajeros automáticos lo contrata para que programen la entrega de
#billetes, el usuario ingresa la cantidad de dinero que desea y usted debe indicar cuantos billetes de cada
#denominación se debe entregar. Es importante entregar siempre la menor cantidad de billetes. Ayuda:
#El operador % da el resto de la división a/b, y el operador // da la parte entera del cociente de a/b

monto=int(input("por favor, ingrese monto a sacar: "))
billete1=1000
billete2=500
billete3=200
billete4=100

bMil=monto//billete1
print("deberá entregar", bMil, "billetes de ",billete1)
resto=monto%billete1

bQuin=resto//billete2
print("deberá entregar", bQuin, "billetes de ",billete2)
resto2=resto%billete2

bDos=resto2//billete3
print("deberá entregar", bDos, "billetes de ",billete3)
resto3=resto2%billete3

bCien=resto3//billete4
print("deberá entregar", bCien, "billetes de ",billete4)
resto4=resto3%billete4

print("se le asignará", resto4, "a una cuenta corriente")