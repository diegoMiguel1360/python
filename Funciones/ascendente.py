import random

def orden (x,y):
    if x>y:
        return "descendente"
    elif x<y:
        return "ascendente"
    else:
        return "iguales"

for i in range (10):
    x = round(random.randrange(10))
    y = round(random.randrange(10))
    print(x,y,orden(x,y))
