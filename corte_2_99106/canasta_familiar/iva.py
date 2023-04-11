def iva(ca):
   comprobar=True
   while comprobar:
      if ca =='00' and ca == '01' and ca== '02':
         print("valores no son validos ")
      elif ca=='20' and ca == '21' and ca== '30' and ca == '22'  and ca== '30'  :
         vb=c/0.05
         print(f'el valor en bruto es de {vb} el iva es del {0.05} y el valor inicial es de {c}')
      elif ca=='20' and ca == '21' and ca== '30' and ca == '22'  and ca== '30'  :
         vb=c/0.19
         print(f'el valor en bruto es de {vb} el iva es del {0.05} y el valor inicial es de {c}')
      else:
         comprobar=False
         print ("fin del proceso")
if __name__=="__name__":
    iva()