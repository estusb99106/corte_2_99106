milista=[3,5,7]
while 1:
    opc=input("ingrese un dato: ")
    if opc =='borrar':
        milista.clear()
    else:
        index=int(input("ingrese un dato: "))
        milista.insert(index,opc)
        print(milista)