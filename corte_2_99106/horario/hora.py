def hor(hor):
    dato=int(input("ingrese el dato que quiere: "))
    if dato==0:
        print(hor.index(0))
    elif dato==1:
        print(hor.index(1))
    elif dato==2:
        print(hor.index(2))
    elif dato==3:
        print(hor.index(3))
    elif dato==4:
        print(hor.index(4))
    elif dato==5:
        print(hor.index(5))
    elif dato==6:
        print(hor.index(6))
    else:
        print('no es un dato disponible')
if __name__=="__main__":
    hor()