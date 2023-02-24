j = [3,0]

def value(j):
    print(j[2])

try:
    value(j)
except IndexError:
    print('la lista no es tan larga')