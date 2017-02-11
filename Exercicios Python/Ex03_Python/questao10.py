def VelocidadeMedia(distancia,tempo):

	velocM = distancia / tempo
	return velocM

distancia = float(input("Digite a distância percorrida em Km: "))
tempo = float(input("Digite a duração da viagem em horas: "))

print(VelocidadeMedia(distancia,tempo))