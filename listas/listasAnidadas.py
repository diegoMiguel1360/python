import random

matriz = [[1,2,3],[4,5,6],[7,8,9]]

for i in matriz:
    for j in i:
        print(j)

col = random.randint(2,5)
lista = [[round(random.random()*100) for i in range (col)] for i in range (col)]
print(lista)
