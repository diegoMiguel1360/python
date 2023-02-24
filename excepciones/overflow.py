j = 5.0

def value (j):
    for i in range(1, 1000):
        j = j**i
        print(j)

try:
    value(j)
except OverflowError:
    print('saturacion')