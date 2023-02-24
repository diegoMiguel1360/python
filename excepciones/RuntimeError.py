def primer_error():
    raise RuntimeError("Ocurrió un error en la función.")

def ejecucion():
    try:
        primer_error()
    except RuntimeError as error:
        print("Se generó un error:", error)

ejecucion()