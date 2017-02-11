def MultiploDe5(num):

	if((num % 5 == 0) or (num /5 == 1)):
		return True
	else:  
		return False

num = int(input("Digite um numero: "))

print(MultiploDe5(num))