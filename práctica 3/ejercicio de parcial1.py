n=int(input("ingrese un valor n: "))
i=1
f=3
p=6
m=2
suma=0
signo=-1

while i<=n:
    serie=-((f*p)/m)*signo
    suma=suma+serie
    f=f+2
    p=p+3
    m=m*2
    signo=signo*(-1)
    i=i+1
print(suma)