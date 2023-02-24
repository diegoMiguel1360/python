def depuracion():
    try:
        purga = []
        while True:
            purga.append(" " * (10 ** 6))  # Agrega un string de un millón de espacios a la lista
    except MemoryError:
        print("Se agotó la memoria disponible.")

depuracion()