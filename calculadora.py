import sys, random, math

#x = valor inicial; y = juros; z= tempo
#definições da calculadora

def optionx(x,y,z):
    diferenca = x/y
    juros = (z/100) + 1
    tempo = math.log(diferenca, juros)
    return print("O montante será de: " + str(x)+ ' reais.' + "\nCom um valor inicial de: " + str(y) + " reais" + "\nNo período de: " + str(tempo) + " meses" + '\n ' )

def optiony(x,y,z):
    juros = (y/100) +1
    potencia = juros ** z
    montante = x * potencia
    return print("O montante será de: " + str(montante) + " reais."
      "\nSeu investimento foi de: "+ str(x) + " reais." + "." "\nNo período de: " + str(z) + " meses." + '\n ' )

def optionz(x,y,z):
    juros = ((y/100) +1)
    juros = juros **z
    valor_inicial = x/juros
    return print("O montante será de: " + str(x) + " reais."+ "\nCom um valor inicial de: " + str(valor_inicial) + " reais. " + "\nNo período de: " + str(z) + " meses" + '\n ')
    
   
#loop calculadora
while True:
   print("A 'option1' calcula o montante, a 'option2' calcula o período e a 'option3' calcula o valor inicial")



   #loop de escolha
   while True:
      print("Escolha uma opção: " +  "Option 1 (digite x), " + "Option 2 (digite y), " + "Option 3 (digite z)")
      print("Se deseja sair, digite 'q'"+ "\nNão são permitidos números negativos ou letras")
      escolha = input()


      #erro de entrada
      
      while escolha not in ['q', 'x','y','z']:
          print("Você deve escolher opções válidas")
          escolha = input()

                  
      if escolha ==  'q':
          sys.exit()  #nota: sempre deixar sys.exit como a primeira opção
      if escolha == 'x' or 'y' or 'z':
          break

    #valor do montante e excessões
   if escolha == 'x':
         print("Escolha o valor do montante")
         valor = input()

         try:
             float(valor)
             valor = float(valor)

         except:
                 print('Você deve digitar números' + '\n')
                 continue


         #while de negativo
         while valor<0:
             print("Você deve usar números positivos")
             valor = float(input("Escolha o valor do montante "))


         #valor inicial e exceções   
         print("Escolha o valor inicial")
         inicio = input()

         try:
             float(inicio)
             inicio = float(inicio)
                
         except:
             print('Você deve digitar números' + '\n')
             continue

         #while de negativo
         while inicio<0:
             print('Você deve usar números positivos')
             inicio = float(input("Escolha o valor inicial "))
    
         
         #taxa de juros e exceção
         print("Agora escolha uma taxa de juros (%)")
         taxa = input()

         try:
             float(taxa)
             taxa = float(taxa)
                
         except:
             print('Você deve digitar números' + '\n')
             continue

         #while de negativo
         while taxa<0:
             print('Você deve usar números positivos')
             taxa = float(input("Escolha a taxa de juros"))
         
             
         optionx(valor,inicio, taxa)


   #valor inicial e exceções
   if escolha == 'y':
         print("Escolha um valor inicial")
         valor =  input()

         try:
             float(valor)
             valor = float(valor)
                
         except:
             print('Você deve digitar números' + '\n')
             continue

         #while de negativo
         while valor<0:
             print('Você deve usar números positivos')
             valor = float(input("Escolha o valor do montante"))
             

        #taxa de juros e exceções   
         print("Agora escolha uma taxa de juros (%)")
         taxa = input()
         
         try:
             float(taxa)
             taxa = float(taxa)
                
         except:
             print('Você deve digitar números' + '\n')
             continue

         #while de negativo
         while taxa<0:
             print('Você deve usar números positivos')
             taxa = float(input("Escolha a taxa de juros "))
             



         #período e exceções    
         print("Escolha um período")
         periodo = input()

         try:
             float(periodo)
             periodo = float(periodo)

         except:
             print('Você deve digitar números' + '\n')
             continue
             

         #while de negativo
         while periodo<0:
             print('Você deve usar números positivos')
             periodo = float(input("Escolha o período "))

         
         optiony(valor, taxa, periodo)


   #montante e exceções
   if escolha == 'z':
         print("Escolha um valor do montante")
         valor =  input()

         try:
             float(valor)
             valor = float(valor)
                
         except:
             print('Você deve digitar números' + '\n')
             continue

         #while de negativo
         while valor<0:
             print('Você deve usar números positivos')
             valor = float(input("Escolha o valor do montante"))

         

        #taxa e exceções
         print("Agora escolha uma taxa de juros (%)")
         taxa = input()

         try:
             float(taxa)
             taxa = float(taxa)
                
         except:
             print('Você deve digitar números' + '\n')
             continue

         
         #while de negativo
         while taxa<0:
             print('Você deve usar números positivos')
             taxa = float(input("Escolha uma taxa de juros "))
         

          #período e exceções   
         print("Escolha um período")
         periodo = input()

         try:
             float(periodo)
             periodo = float(periodo)

                
         except:
             print('Você deve digitar números' + '\n')
             continue

         #while de negativo
         while periodo<0:
             print('Você deve usar números positivos')
             periodo = float(input("Escolha o período "))

             
         optionz(valor, taxa, periodo)


