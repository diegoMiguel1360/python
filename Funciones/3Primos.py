def factoresPrimos(num):
    div=2
    while div<=num:
        if num%div==0:
            print(div)
            num/=div
        else:
            div+=1
num=int(input("ingresa numero"))
factoresPrimos(num)

