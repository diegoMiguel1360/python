#Diseñar una lista de spotify
mi_musica = {'foals':{'in deegres':('indie rock',3,45),
                        'inhaler':('indie',4,18),
                        'my number':('indie rock',3,27)},
            'kasabian':{'club foot':('indie rock',4,54),
                        'lsf':('indie',5,32),
                        'fire':('rock',4,18)}
            }

#Anexar canciones (genero, duracion) 1
def nueva_cancion(cancion,artista,genero,min,seg):
    if artista not in mi_musica:
        mi_musica[artista]={}
    if cancion in mi_musica[artista]:
        print ("---Esta cancion ya existe---")
    else:
        mi_musica[artista][cancion] = (genero,min,seg)
        print('---Cancion agregada correctamente---')
    input('---Enter para continuar---')

#Anexar artista 0
def nuevo_artista(artista):
    if artista in mi_musica:
        input ("---Este artista ya existe---")
    else:
        mi_musica[artista]={}
        input('---Artista agregado correctamente---')

#Buscar artista 2
def buscar_artista(artista):
    if artista in mi_musica:
        for i,j in sorted(mi_musica[artista].items()):
            print(i,'// genero:',j[0],'// duracion:',j[1],':',j[2])
        input('---Enter para continuar---')
    else:
        input('---Artista no existe---')

#Buscar cancion 3
def buscar_cancion(cancion):
    for h,i in mi_musica.items():
        if cancion in i:
            print(h,cancion,mi_musica[h][cancion][0],sep='//',end='//')
            print(mi_musica[h][cancion][1],mi_musica[h][cancion][2],sep=':')
            input('---Enter para continuar---')
            ciclo()
    input('---La cancion no existe---')

#eliminar artista 4
def eliminar_artista(artista):
    if artista in mi_musica:
        del mi_musica[artista]
        input('---Artista eliminado correctamente---')
    else:
        input('---Artista no existe---')

#Ordenar alfabeticamente 5
def ordenar():
    orden = {}
    for h,i in mi_musica.items():
        for j,k in i.items():
            orden[j]=h
    for i,j in sorted(orden.items()):
        print(i,j,sep='//')
    input('---Enter para continuar---')

#Artista que tiene mas canciones 6
def mayor():
    cant = ()
    print('Artista(s) favorito(s):')
    for i in mi_musica.values():
        cant += len(i),
    may = max(cant)
    for i,j in mi_musica.items():
        if may == len(j):
            print(i,'con',may,'canciones')
    input('---Enter para continuar---')
            
#Artista que tiene la cancion mas larga 7
def larga():
    lista = {}
    for h,i in mi_musica.items():
        for j,k in i.items():
            tam = k[1]*60+k[2]
            lista[(h,j)]=tam
            largo = max(lista.values())
    for h,i in lista.items():
        if largo == i:
            for j,k in mi_musica.items():
                if j == h[0]:
                    for l,m in k.items():
                        if i == m[1]*60+m[2]:
                            print(j,'tiene la cancion mas larga =',l,'con ',end='')
                            print(m[1],m[2],sep=':')
    input('---Enter para continuar---')

#Artista que tiene la cancion mas corta 8
def corta():
    lista = {}
    for h,i in mi_musica.items():
        for j,k in i.items():
            tam = k[1]*60+k[2]
            lista[(h,j)]=tam
            corto = min(lista.values())
    for h,i in lista.items():
        if corto == i:
            for j,k in mi_musica.items():
                if j == h[0]:
                    for l,m in k.items():
                        if i == m[1]*60+m[2]:
                            print(j,'tiene la cancion mas corta =',l,'con ',end='')
                            print(m[1],m[2],sep=':')
    input('---Enter para continuar---')

#Menu
def menu(a):
    if a == 0:
        print ("Nombre del nuevo artista: ")
        artista = input()
        nuevo_artista(artista)
    if a == 1:
        print('Nombre del artista?')
        artista = input()
        print('Nombre de la nueva cancion: ')
        cancion = input()
        print('Genero?')
        genero = input()
        print('Cuantos minutos dura?')
        min = int(input())
        print('Cuantos segundos dura?')
        seg = input()
        nueva_cancion(cancion,artista,genero,min,seg)
    if a == 2:
        print ('Nombre del artista que buscas')
        artista = input()
        buscar_artista(artista)
    if a == 3:
        print('Nombre de la cancion que buscas')
        cancion = input()
        buscar_cancion(cancion)
    if a == 4:
        print('Nombre del artista que deseas eliminar')
        artista = input()
        eliminar_artista(artista)
    if a == 5:
        ordenar()
    if a == 6:
        mayor()
    if a == 7:
        larga()
    if a == 8:
        corta()

def ciclo():
    while True:
        print('-----------------------------------','     Bienvenido','   ¿Que deseas hacer hoy?',sep='\n')
        print('0 = Agregar nuevo artista','1 = Agregar nueva cancion','2 = Buscar artista','3 = Buscar cancion','4 = Eliminar un artista','5 = Ver tu lista de reproducción ordenada','6 = ¿Cual es mi artista favorito?','7 = ¿Cual es mi cancion mas larga?','8 = ¿Cual es mi cancion mas corta?','9 = SALIR',sep="\n")
        a = int(input())
        menu(a)
        if a == 9:
            break
ciclo()
print('---DIOS NO EXISTE---')