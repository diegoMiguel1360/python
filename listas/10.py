"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Encuentre la desviación estandar"""

import random

lista = []
suma = 0
cont = 0

for i in range (random.randint(10,25)):
    lista.append(int(random.random()*100))
    suma += lista[i]
    cont += 1
prom = int(suma/cont)
print(lista)

desv = 0
for i in lista:
    if i >= prom:
        dis = i - prom
        
    else:
        dis = prom - i

    dis = dis**2
    desv += dis
desv = desv/len(lista)

print("Desviación estandar = ",round(desv,2))