def ConverteMinutos():


	qtdMinutos = float(input("Digite o valor em minutos: "))

	totalHoras = int (qtdMinutos/60)
	totalMinutos = int (qtdMinutos % 60)

	return str(totalHoras) +" horas e "+ str(totalMinutos) + " minuto(s)" 

print(ConverteMinutos())


