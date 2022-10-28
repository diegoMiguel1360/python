"""¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?"""

suma = 0
cont = 0
prim = 0

for n in range(1,1001):
    for i in range(1,n):
        if n % i == 0:
            cont += 1
        if cont == 2:
            prim += 1
            print (n)
print(prim)