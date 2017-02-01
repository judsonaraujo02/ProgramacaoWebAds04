def retornaQuocienteResto():

	num1 = int(input("Digite o primeiro numero inteiro: "))
	num2 = int(input("Digite o segundo numero inteiro:  "))

	quociente = int(num1 / num2)
	resto = num1 % num2

	return "O quociente da divisao do 2 números é: "+ str(quociente)+" o resto da divisão é: "+ str(resto)   

print( retornaQuocienteResto())