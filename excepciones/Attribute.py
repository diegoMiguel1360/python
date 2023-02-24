x = (1,2)

def tupla(x):
    x.append(4)

try:
    tupla(x)
except AttributeError:
    print('Esta variable es inmutable')
