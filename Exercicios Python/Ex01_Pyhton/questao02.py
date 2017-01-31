qtdCamisasGrandes = float(input("Digite a quantidade de camisas grandes vendidas...: "))
qtdCamisasMedias = float(input("Digite a quantidade de camisas medias vendidas...: "))
qtdCamisasPequenas = float(input("Digite a quantidade de camisas pequenas vendidas...: "))


totalCamisaPequena = qtdCamisasPequenas * 10
totalCamisaMedia = qtdCamisasMedias * 12
totalCamisaGrande = qtdCamisasGrandes * 15

qtdGeralVendas = (qtdCamisasPequenas + qtdCamisasMedias+ qtdCamisasPequenas) 
valorTotalVendas = (totalCamisaPequena + totalCamisaMedia + totalCamisaGrande)

print("Quantidade de camisas pequenas...: ",qtdCamisasPequenas)
print("O valor total arrecadado das vendas de camisas pequenas...: ",totalCamisaPequena)

print("Quantidade de camisas medias...: ",qtdCamisasMedias)
print("O valor total arrecadado das vendas de camisas medias...: ",totalCamisaMedia)

print("Quantidade de camisas qtdCamisasGrandes...: ", qtdCamisasGrandes)
print("O valor total arrecadado das vendas de camisas grandes...: ",totalCamisaGrande)

print("Quantidade total de camisas vendidas...: ",qtdGeralVendas)
print("O valor total das vendas foi...: ",valorTotalVendas)