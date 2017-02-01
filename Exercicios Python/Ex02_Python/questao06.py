def converteVelocidadeKmParaMs():

	velocKm = float(input("Digite a velocidade em km/h:  "))

	velecMs = (velocKm / 3.6)

	return "A velocidade em M/s será: "+ str(velecMs)

print(converteVelocidadeKmParaMs()) 