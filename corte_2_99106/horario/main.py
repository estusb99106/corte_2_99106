from profesor import pro as p
from salon import sal as s
from materia import mart as m
from hora import hor as h
from dia import dia as d
def main():
    materia=["calculointegral","fisicamecanica","tallerfisicamecanica","circuitosDC","programacionaplicadaasistemasmecatroniacos","constitucion","culturaecologica"]
    dia=["lunes","martes y jueves","miercolesy viernes","viernes"]
    pro=[]
    sal=["203ps","306db","305db","305go"]
    hor=["7:00am;9:00am","11:00am;1:00pm","1:00pm;3:00pm","4:00pm;6:00pm"]
    print(p(pro))
    print(m(materia))
    print(d(dia))
    print(s(sal))
    print(h(hor))
if __name__=="__main__":
    main()
