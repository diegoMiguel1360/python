"""supermercado Impares, promedio de compra por cliente, cual es el mas caro y el mas barato"""

factura = {}

while True:
    cliente = input("Ingresa el nombre del cliente: ")
    if cliente == '':
        break
    
    precio = int(input("Ingresa el valor del producto: "))
    if precio == '':
        break
    
    if cliente in factura:
        factura[cliente] += (precio,)
    else:
        factura[cliente] = (precio,)

print(factura)       
for name in sorted(factura.keys()):
    adding = 0
    counter = 0
    for precio in factura[name]:
        adding += precio
        counter += 1
    mayor = max(factura[name])
    menor = min(factura[name])
    print(name, ":", adding / counter,mayor,menor)

