lista=[]
produto=1


for i in range(5):
  numero = int(input("Digite um numero :"))
  produto = produto*numero
  lista.append(numero)

  soma = sum(lista)
  
print("Soma dos numeros da lista :" ,soma)
print("Produto dos numeros da lista:",produto)
  

