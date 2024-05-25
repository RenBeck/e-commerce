from django.contrib import admin
from . import models

class ImagemInline(admin.TabularInline):
    model = models.Imagem

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    min_num = 1
    extra = 0
    can_delete = True

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'tipo', 'descricao',
                    'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [
        VariacaoInline, ImagemInline
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
admin.site.register(models.Imagem)
