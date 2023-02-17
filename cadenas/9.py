'''Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, 
luego tres primeras y así sucesivamente hasta llegar a la última'''

def cadena(a):
    b = ""
    for i in a:
        b += i
        if len(b) > 1 and b.endswith(' ') == False:
            print(b)

cad = input('ingrese un texto:\n')

cadena(cad)