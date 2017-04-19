ListaIdade=[]
ListaAltura=[]


for i in range(3):
  idade= int(input("Digite idade :"))
  ListaIdade.append(idade)
  altura = float(input("Digite altura :"))
  ListaAltura.append(altura)

ListaIdade.reverse()
ListaAltura.reverse()
  
print("idades : " ,ListaIdade)
print("alturas : ",ListaAltura)
  

