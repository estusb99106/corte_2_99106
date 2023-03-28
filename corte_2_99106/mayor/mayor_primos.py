import random as r
from mayor import mayor as m
from primos import prim as p
def main():
    num=[0]*10
    for i in range (10):
        num[i]=r.randint(1,50)
    print(num)
    print(m(num))
    print(p(num))
if __name__=="__main__":
    main()