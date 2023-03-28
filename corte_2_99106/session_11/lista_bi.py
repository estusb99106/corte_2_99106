from random import randint as r
def matrices(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range (columnas):
            num=r(1,10)
            matriz[i].append(num)
    return matriz
def escalar(matriz,n):
    for i in matriz:
        for j in range(len(i)):
            i[j]=n*i[j]
    print(matriz)
def app():
    filas=r(1,10)
    columnas=r(1,10)
    matriz=matrices(filas,columnas)
    print(matriz)
    n=r(1,10)
    escalar(matriz,n)
if __name__=='__main__':
    app()
