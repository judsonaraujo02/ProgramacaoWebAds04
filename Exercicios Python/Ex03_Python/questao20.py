def RetornaIMC(indice):

	if (indice < 18.5):
		return str (indice) + " Você está abaixo do peso!"

	elif (indice >18.5 and indice <= 25):
		return str(indice) + " Você está no peso normal!"

	elif (indice >25 and indice <=30):
		return str (indice) + " Você está com sobre peso!"

	elif (indice > 30 and indice <= 35):
		return str (indice) + " Você é um obeso leve!"	

	elif (indice > 35 and indice <= 39.9):
		return str(indice) +" Você é um obeso moderado!"

	else:
		return str (indice) + " Você é um obeso morbido!"



peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

indice = (peso/(altura*altura))

print(RetornaIMC(indice))