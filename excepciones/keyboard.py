c = 0

def key(c):
    while True:
        c += 1
        print(c)
try:
    key(c)
except KeyboardInterrupt:
    print('saliste del bucle')