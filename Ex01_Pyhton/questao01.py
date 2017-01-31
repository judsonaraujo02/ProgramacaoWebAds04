qtdPao = float(input("Digite a quantidade de paos: "))
qtdBroa = float(input("Digite a quantidade de broas: "))

totalPao= qtdPao * 0.12
totalBroa= qtdBroa * 1.5

totalVendasDia= totalPao + totalBroa

poupanca = totalVendasDia * 0.1

print("Quantidade de paes vendidos:......",qtdPao)
print("Quantidade de boras vendidas:.....",qtdBroa)
print("Valor total de paes vendidos:......",totalPao)
print("Valor total de boras vendidas:.....",totalBroa)
print("Valor para depositar na poupanca:....",poupanca)

