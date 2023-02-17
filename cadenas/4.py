'''Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas'''

def cadena(a):
    print(a.capitalize(),'capitalize')
    print(a.title(),'title')
    print(a.upper(),'upper')
    print(a.lower(),'lower')
    print(a.swapcase(),'swapcase')

a = input('Escriba cualquier texto:\n')

cadena(a)