Notas=[]
count = 0
somaNotas = 0
media = 0
countNotaMaior = 0
countNotaMenor = 0
i = 0

nota = float(input("Digite a nota :"))

while(nota!=-1):
  i = i+1
  Notas.append(nota)
  count = count+1# quantidade de  numeros lidos
  somaNotas = somaNotas + nota#soma dos valores
  
  nota = float(input("Digite a nota :"))
  media = somaNotas/count#media dos valores
if nota > media:
    countNotaMaior = countNotaMaior + 1
elif nota < 7:
    countNotaMenor = countNotaMenor+1
#Notas.reverse()

print("Quantidade de numeros lidos : ", count)
print("Valores informados: ", Notas)
print("Valores informados na ordem inversa : ", Notas.reverse())
print("Soma dos valores : ", somaNotas)
print("Media dos valores : ", media)
print("Qtde de valores acima da média calculada : ", countNotaMaior)
print("Qtde de valores abaixo de 7 : ", countNotaMenor)







  
             
  
             
            
    






  
  
  



