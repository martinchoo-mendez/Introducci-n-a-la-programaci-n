#Escribir en Python un programa que pida al usuario que ingrese tres valores y los guarde en tres
#variables, x, y, y z. El programa deberá intercambiar circularmente los valores de x, y y z, es decir, x
#debe tomar el valor de y, y el de z y z el de x. Y luego mostrarlos en pantalla:
#El valor de x es: <x>
#El valor de y es: <y>
#El valor de z es: <z>
#donde en lugar de <x>, <y> y <z> deberá mostrarse el valor de las respectivas variables.

x=int(input("por favor, ingrese un valor x: "))
y=int(input("por favor, ingrese un valor y: "))
z=int(input("por favor, ingrese un valor z: "))

aux=x
x=y
y=z
z=aux

print("el valor de x es: ", x,"\nel valor de y es: ", y,"\nel valor de z es: ", z)