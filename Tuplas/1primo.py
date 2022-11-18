import random

tupla=tuple(round(random.random()*100)for i in range(random.randint(10,25)))

print(tupla)

for i in tupla:
    cont = 0
    for j in range (1,i):
        if i % j == 0:
            cont += 1
    if cont == 1:
        print("primo",i)