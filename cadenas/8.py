'''Invente un cifrado de texto tipo murcielago o César. 
Puede utilizar alguna formula matemática para este fin.'''

def cadena (a,b):
    for i in b:
        if i in a:
            c = str(a.index(i))
            b = b.replace(i,c)
    print(b)

b = input('Ingrese un texto:\n').upper()
a = "MURCIELAGO"

cadena (a,b)