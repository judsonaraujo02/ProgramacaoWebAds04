def exibeCasaDezena():

	numero = int(input("Digite um número inteiro de 3 digitos: "))

	centena = int(numero%100)
	dezena = int(centena/10)
	
	return "A número da casa dezena é: "+str(dezena)

print(exibeCasaDezena( ))