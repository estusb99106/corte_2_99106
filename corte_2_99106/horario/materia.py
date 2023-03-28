def mart(materia):
    dato=int(input("ingrese el dato que quiere: "))
    if dato==0:
        print(materia.index(0))
    elif dato==1:
        print(materia.index(1))
    elif dato==2:
        print(materia.index(2))
    elif dato==3:
        print(materia.index(3))
    elif dato==4:
        print(materia.index(4))
    elif dato==5:
        print(materia.index(5))
    elif dato==6:
        print(materia.index(6))
    else:
        print('no es un dato disponible')
if __name__=="__main__":
    mart()