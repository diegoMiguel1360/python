def sumaDivisores(n):
    suma = 0
    for i in range (1,n):
        if n % i == 0:
            suma+= i
    return suma

def perfecto(n):
    sum = sumaDivisores(n)
    if sum == n:
        return "Es perfecto"
    else:
        return "No es perfecto"
print(perfecto(6))

def amigos(a,b):
    sum = sumaDivisores()
    

def primo(n):
    cont = sumaDivisores(n)
    if cont == n+1:
        return "Es primo"
    else:
        return "No es primo"
print(primo(7))