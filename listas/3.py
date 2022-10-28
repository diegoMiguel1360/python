"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Sume los pares y saque el promedio de los impares"""

import random

lista = []
suma = 0


for i in range (random.randint(10,25)):
    lista.insert(0,int(random.random()*100))
    