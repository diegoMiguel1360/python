c=float(input("Introduzca temperatura en grados Celcius: "))
def temp(c):
    f=c*1.8+32
    print(f,"grados fahrenheit")
    k=c+273.15
    print(k,"grados kelvin")
    r=c*1.8+491.67
    print(r,"grados rankine")
temp(c)