notas = []

for i in range(4):
  nota = float(input("Digite um numero :"))
  notas.append(nota)

media = sum(notas)/len(notas)
print(media)

