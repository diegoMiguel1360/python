"""Calcular la operación x n sin utilizar la función pow"""
def expo(x,n):
    p = 1
    for i in range(n):
        p *= x
    print(p)
    
x = int(input("Ingrese un nro: "))
n = int(input("Ingrese potencia: "))
expo(x,n)