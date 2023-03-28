def pro(pro):
    dato=int(input("ingrese el dato que quiere: "))
    if dato==0:
        print(pro.index(0))
    elif dato==1:
        print(pro.index(1))
    elif dato==2:
        print(pro.index(2))
    elif dato==3:
        print(pro.index(3))
    elif dato==4:
        print(pro.index(4))
    elif dato==5:
        print(pro.index(5))
    elif dato==6:
        print(pro.index(6))
    else:
        print('no es un dato disponible')
if __name__=="__main__":
    pro()