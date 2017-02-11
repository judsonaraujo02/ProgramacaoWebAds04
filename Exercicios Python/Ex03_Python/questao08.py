def RetornaPosNeg(num):

	if(num > 0):
		return "Numero positivo!"
	
	elif(num < 0):
		return "Numero negativo" 

	else:
		return "Numero igual a zero!"	


num = int(input("Digite um número: "))

print(RetornaPosNeg(num))
