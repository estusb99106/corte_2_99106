def fac(num):
    if num <= 1:
        return num
    else:
	    return num * fac(num-1)
if __name__=="__main__":
     fac()