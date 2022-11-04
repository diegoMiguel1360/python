import random

list = [0 for i in range (10)]
print(list)
list = [i+1 for i in range (10)]
print(list)
list = [(i+1)**2 for i in range (10)]
print(list)

"""Condicionales en una linea"""
pares = [x for x in list if x % 2 == 0]
impares = [x for x in list if x % 2 != 0]
print(pares)
print(impares)

"""si la condición tiene un else, toda la condicion va antes del for"""
pares2 = [x if x % 2 == 0 else 0 for x in list]
print(pares2)

"""llenar una lista con las raices cuadradas de nro de 1 hasta n"""
n = int(random.randint(1,10))

list = [(random.randint(1,20))*0.5 for i in range(n)]
print(list)


