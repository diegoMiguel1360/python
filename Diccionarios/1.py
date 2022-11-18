dic={
    "gato":"cat",
    "perro":"dog",
    "caballo":"horse",
    "vaca":"cow",
}
print(dic)

dic.update({"pato":"duck"}) # update: si ya existe la clave, la actualiza y si no, la incluye al final
print(dic)

for i in dic.keys():
    print(i) #keys() siempre devuelve una lista
    
for i in dic.items():
    print(i) #items() siempre devuelve una tupla
    
for i,j in dic.items():
    print(i,j)

# sorted devuelve en orden alfabetico
print(sorted(dic))
print(sorted(dic.items()))
print(sorted(dic.values()))
print(sorted(dic.keys()))