'''Determinar en que tiempo esta conjugado un verbo'''

v = input('escriba un verbo\n')
pasado=['ado','ido','é','í','áron','éron','ó','ste','mos']
infinitivo=['ar','er','ir']
futuro=['ré','rá','rán','remos','ras']
lista=[pasado,infinitivo,futuro]

def verbo(v,l):
    for i in l:
        for j in i:
            print(j)
            if v.endswith(j):
                return'esta en tiempo pasado'
            elif v.endswith(j):
                return'se encuentra sin conjugar'
            elif v.endswith(j):
                return'esta en tiempo futuro'
    return'esta en tiempo presente'

print(v,verbo(v,lista))