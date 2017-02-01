def converteVelocidadeMsParaKm():

	velocidadeMs = float(input("Digite a velocidade em m/s:  "))

	velocidadeKm = (velocidadeMs * 3.6)

	return "Velocidade em Km/h será:  " + str(velocidadeKm)

print (converteVelocidadeMsParaKm())