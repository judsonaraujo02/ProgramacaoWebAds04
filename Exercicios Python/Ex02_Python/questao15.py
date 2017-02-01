def retornaDigitoDasDezenas():

	numero = int(input("Digite um número de 3 algarismosna forma CDU: "))

	centena = int(numero /100)
	#print(" "+str(centena))
	
	dezena = int((numero%100)/10)
	#print(" "+str(dezena))

	unidade = int(numero % 10)
	#print(" "+str(unidade))
	
	numeroUDC = (unidade*100) + (dezena*10) + (centena*1) 

	return "O número normal na forma CDU: "+ (str(numero)) + " e na forma UDC será: "+str(numeroUDC)

print(retornaDigitoDasDezenas( ))	