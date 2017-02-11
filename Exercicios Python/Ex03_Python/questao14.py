def CapazDeVotar(anoNascimento):

	podeVotar = (2017 - anoNascimento)

	if((podeVotar >= 16 and podeVotar <= 70)):
		
		return "Pode votar!"
	else:
		return "Não pode votar "


anoNascimento = int(input("Digite o ano de nascimento da pessoa: "))

print(CapazDeVotar(anoNascimento))
