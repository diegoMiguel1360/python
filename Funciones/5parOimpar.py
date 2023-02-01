'''suma=1
for i in range(15):
    print(suma)
    suma=suma+i'''
def nro():  
    import random
    numero=int(random.randint(50,100))
    print(numero)
    if numero%2==0:
        print("es par ")
        for i in range(2,numero,2):
            print(i)
    elif numero%2!=0:
        print("impar")
        for j in range(1,numero,2):
            print(j)
nro()
