def Multiplo7(num):

	if (num %7 == 0):
		return "O numero é multiplo de 7!"

	else:
		return "O numero não é multiplo de 7!"


num = int(input("Digite um numero: "))

print(Multiplo7(num))
