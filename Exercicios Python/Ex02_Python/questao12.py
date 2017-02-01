def mediaPonderada():

	num1 = float(input("Digite o 1º número: "))
	peso1 = float(input("Digite o peso 1: "))
	
	num2 = float(input("Digite o 2º número: "))
	peso2 = float(input("Digite o peso 2: "))
	
	num3 = float(input("digite o 3º número: "))
	peso3 = float(input("Digite o peso 3: "))
	
	num4 = float(input("Digite o 4º número: "))
	peso4 = float(input("Digite o peso 4: "))
	
	
	mediaPond = ((num1 * peso1) + (num2 * peso2) + (num3 *peso3) + (num4 * peso4)) / (peso1+peso2+peso3+peso4)

	return "A media ponderada será: "+str(mediaPond)

print(mediaPonderada( ))
