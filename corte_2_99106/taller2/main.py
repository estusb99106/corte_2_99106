from busqueda import bus as b
from ordenar import ord as o
def main():
    dicc={}
    f=open('organization_data.csv','rt')
    matriz=f.readlines()
    f.seek(0)
    print(matriz)
    for i in range (len(matriz)):
        lista=f.readline().rstrip('\n').split(',')
        for j in range(len(lista)):
            pos=str(f'{i}{j}')
            dicc[pos]=lista[j]
    print(dicc)
    f.close()
    ordenados = sorted(dicc, key=lambda name : name[])
    print(ordenados)
if __name__=="__main__":
    main()