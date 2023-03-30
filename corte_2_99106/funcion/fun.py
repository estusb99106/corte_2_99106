def fun(n,p):
     if n<=0:
        return 0
     else:
        num=(n*p)+fun(n-1*p)
        return num
if __name__=="__main__":
    fun()