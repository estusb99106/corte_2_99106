def prim(num):       
    valores=[num]        
    if valores > 1:
        cont = 0
        for i in range(2,valores):
            resto = valores % i
            
            if resto == 0:
                cont+=1
                
        if cont == 0:
            print("Los numeros primos son: ", valores)
   
        else:
            print("Ningún número ingresado es un número primo") 
if __name__=="__main__":
  prim()