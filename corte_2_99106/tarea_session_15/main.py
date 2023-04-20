class Profeciones():
    def __init__(self,nombre:str,edad:int):
        self.__nombre=nombre
        self.__edad=edad
    #--------getters-----
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    #------setters------
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def setEdad(self,edad:int):
        self.__edad=edad
    def Vidas(self):
        print("salve una vida")
class medico(Profeciones):
    def __init__(self, nombre: str, edad: int,especialidad:str,pacientes:int):
        super().__init__(nombre, edad)
        self.__especialidad=especialidad
        self.__pacientes=pacientes

    #--------getters------
    def getEspecialidad(self):
        return self.__especialidad
    def getPacientes(self):
        return self.__pacientes
    #-------setters -----
    def setEspecialidad(self,especialidad:str):
        self.__especialidad=especialidad
    def setPacientes(self,Pacientes:str):
        self.__pacientes=Pacientes
    def Vidas(self):
        print("has salvado otra vida")
class ingeniero(Profeciones):
    def __init__(self, nombre: str, edad: int, campo:str, inventos:int):
        super().__init__(nombre, edad)
        self.__campo=campo
        self.__inventos=inventos
        #--------getters------
    def getCampo(self):
        return self.__campo
    def getInventos(self):
        return self.__inventos
    #-------setters -----
    def setCampo(self,campo:str):
        self.__campo=campo
    def setInventos(self,inventos:str):
        self.__inventos=inventos
class policia(Profeciones):
    def __init__(self, nombre: str, edad: int, sector:str, rango:str):
        super().__init__(nombre, edad)
        self.__sector=sector
        self.__rango=rango
        #--------getters------
    def getSector(self):
        return self.__sector
    def getRango(self):
        return self.__rango
    #-------setters -----
    def setSector(self,sector:str):
        self.__sector=sector
    def setRango(self,rango:str):
        self.__rango=rango
def main():
    doctor=medico('manuel',34,'pediatria',50)
    inge=ingeniero('luis',45,'mecatronica',10)
    poli=policia('jimena',25,'usaquen', 'capitan')
    print(f'medico: {doctor.getNombre()}\n'+\
    f'Edad:{doctor.getEdad()}\n'+\
    f'especialida:{doctor.getEspecialidad()}\n'+\
    f'numero de pacientes:{doctor.getPacientes()}\n'+\
    f'vidas:{doctor.Vidas()}\n')
    print(f'ingeniero: {inge.getNombre()}\n'+\
    f'Edad:{inge.getEdad()}\n'+\
    f'campo especializado:{inge.getCampo()}\n'+\
    f'numero de inventos creado:{inge.getInventos()}\n')
    print(f'policia: {poli.getNombre()}\n'+\
    f'Edad:{poli.getEdad()}\n'+\
    f'sector de trabajo:{poli.getSector()}\n'+\
    f'rango:{poli.getRango()}\n')

if __name__=="__main__":
    main()