"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Encuentre la desviación estandar"""

import random

lista = []
suma = 0

for i in range (random.randint(10,25)):
    lista.append(int(random.random()*100))
    suma += lista[i]
prom = round(suma/len(lista),2)
print(lista)
print(prom)

desv = 0
for i in lista:
    dis = (i - prom)**2
    desv += dis
desv = desv/len(lista)
desv = round(desv ** 0.5,2)

print(desv)
