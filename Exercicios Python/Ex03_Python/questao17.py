def RetornaParOuImpar(num1,num2):

	if (num1 %2 == 0) and (num2 % 2 == 0):
		
		return "O dois números são pares"

	elif (num1 %2 == 0) and (num2 %2 !=0):

		return "O primeiro é par e o segundo é ímpar!"

	elif (num1 %2 !=0) and (num2 %2 ==0):
		
		return "O primeiro é ímapr e o segundo é par!"
	
	else:
		return "Os dois são ímpares! 


num1 = int(input("Digite o primeiro número: ")) 
num2 = int(input("Digite o segundo número: "))

print(RetornaParOuImpar(num1,num2))