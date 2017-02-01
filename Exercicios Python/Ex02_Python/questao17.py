def descontoProduto():

	valorProduto = float(input("Digite o preço do produto: "))
	qtdDesconto = float(input("Digite a porcentagem do desconto: "))

	desconto= (valorProduto*qtdDesconto)/100
	 
	produtoComDesconto = valorProduto - desconto

	return "O valor do produto com desconto é: "+str(produtoComDesconto)

print(descontoProduto( ))