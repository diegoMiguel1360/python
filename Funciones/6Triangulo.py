"""Escribir un programa que visualice la siguiente figura, utilizando ciclos.
El usuario decide cuantas líneas quiere imprimir
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *"""
def triangulo(n):
    x = "* "
    for i in range(n):
        print (x)
        x += "* "
        
n = int(input("Cuantas lineas desea imprimir? "))
triangulo(n)