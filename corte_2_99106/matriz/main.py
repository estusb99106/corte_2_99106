from mar import matrices as m
from fun import mayor as ma
from orden import ord as o
def main():
    filas=5
    columnas=10
    matriz=m(filas,columnas)
    print(matriz)
    print(f'el numero mayor y menor son {ma(matriz)}')
    print(o(matriz))
if __name__=='__main__':
    main()
