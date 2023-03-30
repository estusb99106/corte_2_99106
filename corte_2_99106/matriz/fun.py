def mayor(matriz):
    mayor = [matriz]
    menor = [matriz]
    for i in range(len(matriz)):
        for j in range(len(i)):
            f=(f'{i}{j}')
            if i[j] > mayor:
                mayor = i
            if i[j] < menor:
                menor = i
    print(mayor,menor)
if __name__=="__main__":
    mayor()