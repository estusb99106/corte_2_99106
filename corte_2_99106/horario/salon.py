def sal(sal):
    dato=int(input("ingrese el dato que quiere: "))
    if dato==0:
        print(sal.index(0))
    elif dato==1:
        print(sal.index(1))
    elif dato==2:
        print(sal.index(2))
    elif dato==3:
        print(sal.index(3))
    elif dato==4:
        print(sal.index(4))
    elif dato==5:
        print(sal.index(5))
    elif dato==6:
        print(sal.index(6))
    else:
        print('no es un dato disponible')
if __name__=="__main__":
    sal()