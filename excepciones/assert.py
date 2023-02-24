a = input("Digite su nombre en mayúscula sostenida\n")

def mayus(x):
    assert x.isupper()
    return x
try:
    print(mayus(a))
except AssertionError:
    print('El texto incluye al menos una letra minúscula')