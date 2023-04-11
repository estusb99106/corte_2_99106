
class Persona:
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.frase=None
        
    def hablar(self):
        return self.frase


def main():
    estudiante=Persona()
    estudiante.nombre="javier"
    estudiante.apellido="Gomez"
    estudiante.edad=21   
    estudiante.frase='oh debo estudiar'

    futbolista=Persona()
    futbolista.nombre="Radamel" 
    futbolista.apellido="Garcia"
    futbolista.edad=36
    futbolista.frase='goooooooool'

    print(id(estudiante))
    futbolista()

if __name__=="__main__":
    main()