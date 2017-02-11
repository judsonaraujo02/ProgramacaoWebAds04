def ParEDivisivelPor3(num):

	if ((num % 2 == 0) and (num %3 == 0)):
		return "É par e divisível por 3"
	else:
		return "Não é divisível por 3!"


num = int(input("Digite um número: "))

print(ParEDivisivelPor3(num))