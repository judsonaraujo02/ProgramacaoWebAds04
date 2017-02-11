def ExibeNumCrescente(num1, num2, num3):

	if (num1 < num2) and (num1 < num3):
		
		if(num2 < num3):
			return (num1, num2, num3)

		else:
			return (num1, num3, num2)

	elif (num2 < num1) and (num2 < num3):
		
		if(num2 < num3):
			return (num2, num1, num3)

		else:
			return (num2, num3, num1)

	else:
		
		if(num1 < num2):
			return (num3,num1,num2)
		else:
			return (num3,num2,num1)
	

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digiteo o segundo numero: "))
num3 = float(input("Digite o o terceiro numero: "))


print(ExibeNumCrescente(num1, num2, num3))