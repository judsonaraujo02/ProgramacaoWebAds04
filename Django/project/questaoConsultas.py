from .core.models import *

#questao 02
#letra a) Um cliente

cliente = Cliente(cpf="0051234500", nome="Juliana Melo", endereco="Rua 8", complemento="Q-H", cidade="teresina", estado="pi", cep="64057185", foneResidencial = "32315060", foneTrabalho="40054020", rendaFamiliar="2500", email="julianamelo@gmail.com")
cliente.save()

#letra b) Um fornecedor

fornecedor = Fornecedor(cnpj="00071234567815", nome="Docepan", endereco="Rua Isaias Coelho", complemento="n 1234", cidade ="teresina", estado="pi", cep="64057900", fone="32322030", responsavel="Bruno", webSite="www.docepan.com.br")
fornecedor.save()

#letra c) Um produto

produto = Produto(nomeProduto="Pao de forma", quantidade=100, minQuantidade =10)
produto.save()

#letra d)Um pedido

pedido = Pedido(dataPedido="2017-04-18", dataRecebimento="2017-04-20", precoTotal=500, codigoFornecedor=fornecedor)
pedido.save()

#letra e) Incluir itens de um pedido

item_pedido = itemPedido(codPedido=pedido, codProduto=produto, precoUnitario=5, quantidade=50)
item_pedido.save()

#letra f) Uma venda

venda = Venda(dataVenda="2017-04-03", valorTotal=600, codCliente= cliente)
venda.save()

#letra g) Incluir intens em uma venda

item_venda = ItemVenda(codigoVenda=venda, codigoProduto=produto, precoUnitario=5, quantidade=40)
item_venda.save()

#questao 3

#letra a)

cliente = Cliente.object.all()
for i in clientes:
	print(i.id, i.nome)

#letra 	b)

vendas_rai = Vendas.objects.filter(codCliente=3)
for i in vendas_rai:
	print(i.codigoVenda)

#letra c) um pedido

pedidos = Pedido.objects.get(pk=1)
print(pedidos.codigo, pedido.dataPedido)

# letra d) todos os itens pedidos

itens_pedido = ItemPedido.objects.all()
for i in itens_pedido:
	print(i.id)

# letra e) Produtos que atingiram o estoque minimo
estoque_min = Produto.objects.filter(quantidade=10)
for i in estoque_min:
	print(i.nomeProduto, i.quantidade)



