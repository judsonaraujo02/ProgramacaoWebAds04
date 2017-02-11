def ValidaVogal(letra):

	if((letra == "A") or (letra == "E") or (letra == "I") or (letra == "O") or (letra == "U")):

		return "É vogal!"

	else:
		return "Não é vogal!"		

letra = input("Digite uma letra: ")
letra = letra.upper()

print(ValidaVogal(letra))
