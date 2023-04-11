from busqueda import bus as b
from iva import iva as v
def main():
    dicc={}
    f=open('Alimentos.txt','rt')
    matriz=f.readlines() 
    f.seek(0)
    print(len(matriz))
    for i in range (len(matriz)):
        lista=f.readline().rstrip('\n').split(',')
        for j in range(len(lista)):
            pos=str(f'{i}{j}')
            dicc[pos]=lista[j]
    print(dicc)
    f.close()
    c=int(input('ingrese el valor del producto '))
    ca=b(dicc)
    iv=v(ca,c)
    print(ca)
    print(iv)


if __name__=="__main__":
    main()