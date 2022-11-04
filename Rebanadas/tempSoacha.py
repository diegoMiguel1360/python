import random

temp = []

for i in range(30):
    temp.append(random.randint(5,28))
print(temp)

a = temp[:15]
b = temp[16:]
c = temp[:10]
d = temp[10:20]
e = temp[20:]

list = [a,b,c,d,e]

for j in list:
    suma = 0
    for i in j:
        suma += i
    print(round(suma/len(j),2))