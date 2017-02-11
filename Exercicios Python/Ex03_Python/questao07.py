def RetornaNomeESexo(nome,sexo):

	if((sexo == 'm') or (sexo == 'M')):
		return "Ilmo Sr. "+ nome
		
	elif((sexo == 'f') or (sexo == 'F')):
		return "Ilma Sra. "+ nome

	else:
		return "Caractere inválido para sexo"
		

nome = input(" Digite o nome da pessoa: ")
sexo = input("Digite o sexo da pessoa m/M (masculino) ou f/F (feminino)= ")


print(RetornaNomeESexo(nome,sexo))
