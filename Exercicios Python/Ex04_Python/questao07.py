def ImprimeAteLimitedado(numLimit,inc):

	for inc in range(numLimit):
		print(inc)
		inc = inc +1


numLimit = int(input("Digite o número do limite superior: "))
inc = int(input("Digite o incremento: "))

print(ImprimeAteLimitedado(numLimit,inc))	