ListaA=[]#primeiro vetor
ListaB=[]#segundo vetor
ListaC=[]#vetor resultante

for i in range(6):
  numero= int(input("Digite um numero :"))#ler o primeiro vetor com 6 num
  ListaA.append(numero)
  numero= int(input("Digite um numero :"))#ler o segundo vetor com 6 num
  ListaB.append(numero)

  #intercalacao
for i in range(6):#intercala as duas listas
  ListaC.append(ListaA[i])
  ListaC.append(ListaB[i])
  
print("Terceira lista : ",ListaC)
  

