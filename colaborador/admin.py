from django.contrib import admin

from . import models

class Detalhe_cargoInline(admin.TabularInline):
    model = models.Detalhe_cargo


class Inf_bancariasInline(admin.TabularInline):
    model = models.Inf_bancarias


class BeneficiosInline(admin.TabularInline):
    model = models.Beneficios


class EnderecoInline(admin.TabularInline):
    model = models.Endereco


class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'ddd', 'celular', 'get_salario_formatado']
    inlines = [
        EnderecoInline, Inf_bancariasInline, Detalhe_cargoInline, BeneficiosInline
    ]

admin.site.register(models.Perfil_colaborador, PerfilAdmin)
admin.site.register(models.Endereco)
admin.site.register(models.Inf_bancarias)
admin.site.register(models.Detalhe_cargo)
admin.site.register(models.Beneficios)