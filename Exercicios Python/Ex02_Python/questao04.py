def converteMinutos():

	qtdMinutos = float(input("Digite a quantidade em minutos: "))

	valorHoras = int(qtdMinutos/60)
	valorMinutos = (qtdMinutos%60)

	return  str(valorHoras)+" hora(s) e " + str(valorMinutos)+" minutos."

print(converteMinutos())