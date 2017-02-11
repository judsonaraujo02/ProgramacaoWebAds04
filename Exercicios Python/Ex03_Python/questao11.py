def MedeFebre(temp):

	if(temp > 36.5):
		return "Está com febre!" 

	else:
		return "Não esta com febre!"


temp = float(input("Digite a temperatura da pessoa: "))

print(MedeFebre(temp))