def rectangulo (a,b):
    for i in range (a):
        print('')
        for j in range (b):
            print ('*  ',end='')
    print('')

def triangulo (a):
    for i in range (a):
        print('')
        for j in range (a):
            print('*  ',end='')
        a -= 1
    print('')
        
def piramide (a):
    for i in range (a+1):
        print('')
        for j in range (i):
            print('*  ',end='')
    print('')

def cuadrado (a):
    for i in range (a):
        print('')
        for j in range (a):
            print ('*  ',end='')
    print('')
    
def cuadro (a):
    n = '* '
    v = '  '
    for i in range (a):
        print(v)
        for j in range (a):
            if j == 0 or i == 0 or i == a-1 or j == a-1:
                print (n,end='')
            else:
                print (v,end='')
    print(v)