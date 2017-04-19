#12. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

ListaA=[]#primeiro vetor
ListaB=[]#segundo vetor
ListaC=[]#terceiro vetor
ListaD=[]#vetor resultante

for i in range(3):
  numero= int(input("Digite um numero :"))#ler o primeiro vetor com 6 num
  ListaA.append(numero)
  numero= int(input("Digite um numero :"))#ler o segundo vetor com 6 num
  ListaB.append(numero)
  numero= int(input("Digite um numero :"))#ler o segundo vetor com 6 num
  ListaC.append(numero)

  #intercalacao
for i in range(3):#intercala as duas listas
  ListaD.append(ListaA[i])
  ListaD.append(ListaB[i])
  ListaD.append(ListaC[i])
  
  
print("Terceira lista : ",ListaD)
  

