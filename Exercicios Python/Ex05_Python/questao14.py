"""14. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média
anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""

TempMediaDoAno=[]
media = 0

for i in range(1,5):
  tempMedia = float(input("Digite a temperatura do mes" + str(i) + ":"))
  TempMediaDoAno.append(tempMedia)

  media = sum(TempMediaDoAno)/len(TempMediaDoAno)#calcula a media anual

for i in range(1,5):
  if TempMediaDoAno[i] > media:
    print("%d : %.1f"%(i+1,TempMediaDoAno[i])) 
print(media)
    
    






  
  
  



