def dia(dia):
    dato=int(input("ingrese el dato que quiere: "))
    if dato==0:
        print(dia.index(0))
    elif dato==1:
        print(dia.index(1))
    elif dato==2:
        print(dia.index(2))
    elif dato==3:
        print(dia.index(3))
    elif dato==4:
        print(dia.index(4))
    elif dato==5:
        print(dia.index(5))
    elif dato==6:
        print(dia.index(6))
    else:
        print('no es un dato disponible')
if __name__=="__main__":
    dia()