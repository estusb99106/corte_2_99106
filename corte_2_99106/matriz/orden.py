def ord(matriz):
    comprobar=False
    while comprobar==False:
        comprobar=True
        for i in range(len(matriz)-1):
            if matriz[i]>matriz[i+1]:
                aux=matriz[i]
                matriz[i]=matriz[i+1]
                matriz[i+1]=aux
                comprobar=False
    print(matriz)
if __name__=='__main__':
    ord()
