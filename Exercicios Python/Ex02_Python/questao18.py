def inverteValor(valorA,valorB):

	valorB = valorA + valorB
	valorA = valorB - valorA
	valorB = valorB - valorA
	
	return valorA, valorB

valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))

print("O valor de A será: %d; O valor de b será: %d" %inverteValor(valorA,valorB))	