def mayor(num):
    if len(num)>0:
        menor=num[0]
        mayor=num[0]
        for n in num:
            if n<menor:
                menor=n
            if n>mayor:
                mayor=n
        return menor , mayor
    else:
        return None
if __name__=="__main__":
    mayor()