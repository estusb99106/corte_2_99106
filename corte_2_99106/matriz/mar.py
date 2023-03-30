from random import randint as r
def matrices(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range (columnas):
            num=r(1,50)
            matriz[i].append(num)
    return matriz
if __name__=="__main__":
    matrices()