qtdLatas = float(input("Digite a quantidade de latas compradas:  "))
qtdGarrafas = float (input("Digite a quantidade de garrafas 600ml compradas:  "))
qtdGarrafasPets = float(input("Digite a quantidade de garrafas pets 2l compradas:  "))

qtdLitrosLata = (qtdLatas * 350)
qtdLitrosGarrafa =(qtdGarrafas * 600)
qtdLitrosGarrafaPets = (qtdGarrafasPets * 2000)

qtdTotalLitros = (qtdLitrosLata + qtdLitrosGarrafa + qtdLitrosGarrafaPets) / 1000

print("Valor total de litros de refigerante comprado:  ",qtdTotalLitros)