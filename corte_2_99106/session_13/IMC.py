
class Pesornas:
    def __init__(self):
        self.nombre=None
        self.altura=None
        self.peso=None

        
    
    def Indece(self):
        IMC=self.peso/((self.altura/100)**2)
        if IMC <= 18.5:
            return str('por debajo ')
        elif IMC <= 24.9:
            return str('Saludable ')
        elif IMC <= 29.9:
            return str('sobrepeso ')
        elif IMC <= 34.9:
            return str('obesidad I ')
        elif IMC <= 39.9:
            return str('obesidad II ')
        else:
            return str('obesidad III ')

def main():
    estudiante1=Pesornas()
    estudiante1.nombre='Pedro Caceres'
    estudiante1.altura= 188
    estudiante1.peso= 97

    estudiante2=Pesornas()
    estudiante2.nombre='Maria Perez'
    estudiante2.altura= 160
    estudiante2.peso= 47

    estudiante3=Pesornas()
    estudiante3.nombre='Julian Dominguez'
    estudiante3.altura= 158
    estudiante3.peso= 58

    estudiante4=Pesornas()
    estudiante4.nombre='Jessica fuentes'
    estudiante4.altura= 170
    estudiante4.peso= 73

    estudiante5=Pesornas()
    estudiante5.nombre='Andres Benavides'
    estudiante5.altura= 168
    estudiante5.peso= 68

    print(f'estudiante: {estudiante1.nombre} resultado: {estudiante1.Indece()}')
    print(f'estudiante: {estudiante2.nombre} resultado: {estudiante2.Indece()}')
    print(f'estudiante: {estudiante3.nombre} resultado: {estudiante3.Indece()}')
    print(f'estudiante: {estudiante4.nombre} resultado: {estudiante4.Indece()}')
    print(f'estudiante: {estudiante5.nombre} resultado: {estudiante5.Indece()}')

if __name__=='__main__':
    main()