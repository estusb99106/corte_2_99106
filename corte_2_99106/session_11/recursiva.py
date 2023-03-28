def cuenta(num):
    num-=1
    if num>0:
        print(num)
        cuenta(num)
    else:
        print("boooooom!")
    print("fin de la funcion", num)
cuenta(5)