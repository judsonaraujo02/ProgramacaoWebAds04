def CalculoUla(num,valorAMultiplicar):

	multiplicacao = 0
		
	for i in range(valorAMultiplicar):
		multiplicacao = multiplicacao + num
		i = i+1
	print("A multiplicacao será: ",multiplicacao)





num = int(input("Digite o número a ser multiplicado: "))
valorAMultiplicar = int(input("Digite o número pelo qual ele sera multiplicado: "))

print(CalculoUla(num,valorAMultiplicar))
