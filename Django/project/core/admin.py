from django.contrib import admin
from .models import *

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('CPF', 'nome', 'email')

class VendaAdmin(admin.ModelAdmin):
    list_display = ('dataVenda', 'valorTotal', 'cliente')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('dataPedido', 'dataRecebimento', 'precoTotal', 'fornecedor')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'minQuantidade')

class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'precoUnitario', 'quantidade')

class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ('venda', 'produto', 'precoUnitario', 'quantidade')


admin.site.register(Cliente)
admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(ItemVenda)
admin.site.register(Fornecedor)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
