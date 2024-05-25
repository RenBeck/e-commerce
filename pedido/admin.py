from django.contrib import admin
from . import models


class ItemPedidoInline(admin.TabularInline):
    model = models.ItemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]

class EntregaAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'usuario', 'status', 'cod_rastreamento']

admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.ItemPedido)
admin.site.register(models.Entrega, EntregaAdmin)
