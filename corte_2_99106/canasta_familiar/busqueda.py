from iva import iva as v
def bus(dicc):
    n=''
    while n!='salir':
        n=input('ingrese un key de busqueda ')
        if n=='salir':
            break
        elif n not in dicc:
            print('error, fuera de rango')
        else:
            print(dicc[n])
            print(v(dicc[n]))
if __name__=="__main__":
    bus() 