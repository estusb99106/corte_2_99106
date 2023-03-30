def bus(dicc):
    n=''
    while n!='salir':
        n=input('ingrese un key de busqueda')
        if n=='salir':
            break
        elif n not in dicc:
            print('error, fuera de rango')
        else:
            print(dicc[n])
        print('43'in dicc)
if __name__=="__main__":
    bus()