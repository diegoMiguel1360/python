#https://docs.python.org/es/3/library/exceptions.html
a=int(input("ingrese un valor menor a 20 "))
# IndentationError
def error(psdf):
    if a <=20:
    print("error")
    else:
    print("esta bien")

    
try: 
    error(a)
except IndentationError:
    print("esta mal")

