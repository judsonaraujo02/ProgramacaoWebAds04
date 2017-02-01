def retornaDivisaodaSoma():

	num1 = float (input("Digite o primeiro número: "))
	num2 = float (input("Digite o segundo número: " ))
	
	soma = (num1 + num2)
	subtracao = (num1 - num2) 

	divisao = (soma *(-1))/(subtracao*(-1)) 

	return "O resultado será:  "+ str(divisao)

print(retornaDivisaodaSoma())