def ComparaMaior(num1, num2):

	maior = 0

	if num1 > num2:
	 	maior = num1
	
	else:
		maior = num2
	
	return maior 


num1 = input("Digite o primeiro numero:")
num2 = input("Digite o segundo numero: ")

print(ComparaMaior(num1, num2))
