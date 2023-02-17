""" Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez"""

def cadena(a,b):
    a=a.lower()
    for i in a:
        if i.isalpha() == True:
            if i not in b:
                b += i
    print(len(b))

cad = "Si desea su propia implementación para ordenar de la función clave, puede ordenar el iterable dado."
cad2 = ""

cadena(cad,cad2)