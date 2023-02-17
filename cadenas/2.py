''' Pida una cadena por teclado y diga cual es su valor al sumar sus codigos.
Cual es el valor numerico de acuerdo a los códigos del alfabeto'''


def cadena (a):
    sum = 0
    for i in a:
        print(i,'=',ord(i))
        sum += ord(i)
    print('total =',sum)

cad=input("Escriba cualquier cosa:\n")

cadena(cad)