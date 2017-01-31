def RetornaPorcento():

	qtdReal = float(input("Digite o valor em reais: "))

	valor = (qtdReal * 0.7)

	return "70%  deste valor será: "+str(valor)

print(RetornaPorcento())