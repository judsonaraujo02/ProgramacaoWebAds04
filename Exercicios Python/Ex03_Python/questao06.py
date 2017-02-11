def RetornaMensagem(valor):

	if (valor<20):
		return "Fique em casa vendo tv!"

	else:
		return "Vá ao cinema!"


valor = float(input("Digite o valor recebido: "))

print(RetornaMensagem(valor))