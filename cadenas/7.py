'''De una cadena diga cuantas vocales tiene, cuantas consonantes, 
cuantas vocales con tilde y cuantos caracteres especiales.'''

def cadena(a):
    a = a.lower()
    vocal=""
    cons=""
    esp=""
    tilde=""
    num=""
    for i in a:
        if i.isalpha()==True:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                vocal += i
            elif i=='á' or i=='é' or i=='í' or i=='ó' or i=='ú':
                tilde += i
            else:
                cons += i
        elif i.isdigit()==True:
            num += i
        elif i==" ":
            continue
        else:
            esp += i
    print('Vocales:',len(vocal))
    print('Consonantes:',len(cons))
    print('Tildes:',len(tilde))
    print('Numeros:',len(num))
    print('caracteres especiales:',len(esp))

cad = 'bravo!!! Bravo!!! Bravo!!!! 😌😉vaya que realmente les recomiendo esta peli de terror/drama (que aunque con un toque sobrenatural) no pierde en su trama lo bien dirigida e inteligente que incluso nos "transportará" automáticamente a ese sótano para "sentir" un poco la desesperación de los niños. Esta basada en el cuento corto llamado ‘The Black Phone’ de Joe Hill, quién es el hijo del autor de terror Stephen King 😌, y que por cierto en el cuento de Joe Hill, The Grabber (El Raptor/Capturador) esta inspirado en John Wayne Gacy, un asesino en serie conocido como el payaso asesino (Killer Clown) que asesinó al menos a 33 jóvenes y niños entre 1972 y 1978. Le platico un poco la trama: En una ciudad de Colorado, en los años 70, un enmascarado secuestra a Finney Shaw, un chico tímido e inteligente de 13 años, y le encierra en un sótano insonorizado donde de nada sirven sus gritos. Cuando un teléfono roto y sin conexión empieza a sonar, Finney descubre que a través de él puede oír las voces de las anteriores víctimas, las cuales están decididas a impedir que Finney acabe igual que ellas.'

cadena(cad)