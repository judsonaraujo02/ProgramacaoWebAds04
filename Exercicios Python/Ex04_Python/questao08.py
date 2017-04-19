def SomaNumPares(num1,num2):

		soma=0
		
		for num1 in range(num1+1,num2):

			if(num1%2 == 0):
				soma = soma+num1
				
		num1 = num1+1
		
			
		print("Soma dos nº pares do intervalo: ",soma)


num1 = int(input("Digite o limite inferior do intervalo: "))
num2 = int(input("Digite o limite superior do intervalo: "))


print(SomaNumPares(num1,num2))