def calculaIdade():

	ano = float(input("Digite o ano do seu nascimento: "))

	if ano > 2013:
	
		print("Você ainda não nasceu!")
		return " "
	
	else: 
		idade2013 = ((ano - 2013) * (-1))
		return "Sua idade em 31/12/2013 era:  "+str(idade2013)

print(calculaIdade( ))
