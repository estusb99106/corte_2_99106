from random import randint as r
milista=[3,5,21,34,5,56,7,9,7]
opc=''
while opc!='salir':
    opc=input("que metodo quiere usar ")
    if opc=='agregar':
        dato=int(input("¿cual dato quiere agregar? "))
        milista.append(dato)
        print(milista)
    elif opc =='borrar':
        dato=int(input("¿cual dato quiere borrar? "))
        milista.remove(dato)
        print(milista)
    elif opc=='limpiar':
        milista.clear()
        print(milista)
    elif opc== 'buscar':
        dato=int(input('¿cual dato quiere buscar? '))
        pos=milista.index(dato)
        print(f'el indice es {pos}')
    elif opc=='insertar':
        dato=int(input('¿cual dato quiere insertar? '))
        index=int(input("ingrese un dato: "))
        milista.insert(index,dato)
        print(milista)
    elif opc=='sacar':
        indice=int(input('¿ingrese el dato que quiere sacar? '))
        milista.pop(indice)
        print(milista)
    elif opc=='comparar':
        menor=min(milista)
        mayor=max(milista)
        print(f'el menor es {menor}\nel mayor es {mayor}')
    elif opc =='tamaño':
        t=len(milista)
        print(f'el tamaño de la lista es {t}')
    elif opc == 'conteo':
        dato=int(input('¿que datos quiere contar? '))
        con=milista.count(dato)
        print(f'el numero de datos repetidos es {con}')
    elif opc=='suma':
        print(f'la suma de la lista es {sum(milista)}')
    elif opc=='comprobar':
        dato=int(input('¿ingrese el valor a buscar?'))
        elm=dato in milista
        print(elm)
    elif opc=='extender':
        lista=int(input('ingrese el numero de datos de la segunda lista '))
        lista2=[]
        for i in range (lista) :
            lista2=r(0,120)
            print(lista2)
        print(lista2.extend(milista))
        
    elif opc=='ordenar':
        ord=milista.sort()
        print(ord)
    elif opc=='invertir':
        inv=milista.reverse()
        print(inv)