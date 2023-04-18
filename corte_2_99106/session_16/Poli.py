class Ciudadano():
    def __init__(self,nombre:str,idioma:str):
        self.__nombre=nombre
        self.__idioma=idioma
    #----------Getters-------------
    def getNombre(self):
        return  self.__nombre
    
    def getIdioma(self):
        return  self.__idioma
    
    #--------setters----
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setIdioma(self,idioma:str):
        self.__idioma=idioma
    
    #--------sobrecarga------

    def saludo(self):
        return "Quoi de beau!"
class Colombia(Ciudadano):
    def __init__(self, nombre: str, idioma: str, cc:int):
        super().__init__(nombre, idioma)
        self.__cc=cc
    def getCC(self):
        return self.__cc
    
    def setCC(self,cc:int):
        self.__cc=cc

    def saludo(self):
        return "Qiubo parce"


class Inglaterra(Ciudadano):
    def __init__(self, nombre: str, idioma: str, id:int):
        super().__init__(nombre, idioma)
        self.__id=id
    def getID(self):
        return self.__id
    
    def setID(self,id:int):
        self.__id=id
    
    def saludo(self):
        return "Hello my friend"

class Chino(Ciudadano):
    def __init__(self, nombre: str, idioma: str, shengfenzheng:int):
        super().__init__(nombre, idioma)
        self.__shengfenzheng=shengfenzheng
    def getShengfenzheng(self):
        return self.__shengfenzheng
    
    def setShengfenzheng(self,shengfenzheng:int):
        self.__shengfenzheng=shengfenzheng
    
    def saludo(self):
        return "NiGanMaYa"

def DarSaludo(obj):
    print(obj.saludo())

def main():
    colombiano=Colombia('Kevin','Español',585446)
    ingles=Inglaterra('Richard','English',741856)
    chino=Chino('Liu','Mandarin',7946516889)
    Ciudadana1=Ciudadano('Carla','Frances')
    DarSaludo(colombiano)
    DarSaludo(ingles)
    DarSaludo(chino)
    DarSaludo(Ciudadana1)

if __name__=="__main__":
    main()