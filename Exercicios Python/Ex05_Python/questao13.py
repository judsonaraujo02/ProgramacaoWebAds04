Idade=[]
Altura=[]
media = 0
countAluno = 0


for i in range(1,6):
  idade= int(input("Digite a idade do " + str(i)+"0 aluno :"))
  Idade.append(idade)
  altura= float(input("Digite a altura do " + str(i)+"0 aluno :"))
  Altura.append(altura)

  mediaAltura =sum(Altura)/len(Altura) 

  if idade >13 and altura < mediaAltura:
    countAluno = countAluno + 1

print("Media da altura : ",mediaAltura)  
print("Quantidade de alunos acima de 13 e com altura inferior a media :",countAluno)
  

