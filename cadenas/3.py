''' cuantas veces se repite un caracter dado'''

def cadena(a,b):
    print(a.count(b))

cad = '''Declinación de Responsabilidades: Los servicios de MISENA son soportados tecnológicamente por © Google y ofrecidos por el Servicio Nacional de
 Aprendizaje – SENA de manera gratuita a los aprendices e instructores 1 54521 de programas de formación titulada, las opiniones que contenga este
  mensaje son exclusivas de su autor y no representan la opinión del Servicio Nacional de Aprendizaje o de sus autoridades. El receptor 
  deberá verificar posibles virus informáticos que tenga el correo o cualquier anexo, razón por la cual el SENA no es responsable de los 
  daños causados por cualquier virus transmitido en este correo electrónico.'''

a = cad.lower()
cad2 = input('Escriba un caracter:\n')
b = cad2.lower()

cadena(a,b)