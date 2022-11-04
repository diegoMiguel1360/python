"""nro de 0 a 100, en un vector mayores de edad y en otro los menores"""
import random

edad = [random.randint(0,100) for i in range(10)]
print(edad)

edad = ["mayor" if x >= 18 else "menor" for x in edad]
print (edad)