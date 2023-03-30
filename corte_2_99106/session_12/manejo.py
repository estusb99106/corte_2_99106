from busqueda import bus as b
def main():
    dicc={}
    f=open('matrizAsignacion.txt','rt')
    # for i in f:
    #     matriz=f.readlines()
    #     print(matriz)
        
    # matriz=f.readlines()
    # print(matriz)
    # print(len(matriz))
    # for i in range(len(matriz)):
    #     print(matriz[i])
    matriz=f.readlines()
    f.seek(0)
    print(len(matriz))
    suma=0
    for i in range (len(matriz)):
        lista=f.readline().rstrip('\n').split(',')
        for j in range(len(lista)):
            pos=str(f'{i}{j}')
            dicc[pos]=lista[j]
    print(dicc)
    f.close()
    b(dicc)



if __name__=="__main__":
    main()