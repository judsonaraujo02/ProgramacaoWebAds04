def RetornaMaior(num1,num2,num3):

	maior = num1

	if(num2 > maior) and (num2 > num3):
		
		maior = num2
		return str (maior) + " maior" 
			
	elif(num3 > maior): 
		maior = num3 
		return str (maior) + " maior"

	else:
		return maior


num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))


print(RetornaMaior(num1,num2,num3))
