def exibeAntecessorESucessor():

	numero = float(input("Digite um número: "))
	
	antecessor = (numero-1)
	sucessor = (numero + 1)

	return "A antecessor é: "+str(antecessor)+ " e o sucessor é:  "+str(sucessor)

print(exibeAntecessorESucessor())
