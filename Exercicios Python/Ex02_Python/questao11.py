def dadosPessoais(): 

	nome =  input("Digite seu nome: ")
	endereco = input("Digite seu endereço: ")
	telefone = input("Digite seu telefone: ")

	return ("Nome: "+str(nome)+ "; Endereço: "+str(endereco)+ "; Telefone: "+str(telefone))

print(dadosPessoais( ))