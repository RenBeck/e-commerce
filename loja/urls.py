from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from pagar.views import paymentController, pagar

from colaborador.models import Perfil_colaborador, Detalhe_cargo, Inf_bancarias, Beneficios, Endereco
from produto.models import Produto, Variacao, Imagem
from trabalheconosco.models import Vaga, Curriculo
from perfil.models import Perfil
from pedido.models import Pedido, ItemPedido, Entrega
from nossaloja.models import Loja
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin


class Detalhe_cargoInline(admin.TabularInline):
    model = Detalhe_cargo
    min_num = 1
    extra = 0

class Detalhe_cargoAdmin(admin.ModelAdmin):
    list_display = ['cargo', 'perfil']

class Inf_bancariasInline(admin.TabularInline):
    model = Inf_bancarias
    min_num = 1
    extra = 0

class Inf_bancariasAdmin(admin.ModelAdmin):
    list_display = ['perfil', 'banco', 'numero_agencia', 'numero_conta']

class BeneficiosInline(admin.TabularInline):
    model = Beneficios
    min_num = 1
    extra = 0

class BeneficiosAdmin(admin.ModelAdmin):
    list_display = ['perfil', 'beneficio']

class EnderecoInline(admin.TabularInline):
    model = Endereco
    min_num = 1
    extra = 0

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['perfil', 'rua', 'numero', 'bairro', 'cidade']

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'ddd', 'celular', 'get_salario_formatado']
    inlines = [
        EnderecoInline, Inf_bancariasInline, Detalhe_cargoInline, BeneficiosInline
    ]


class ImagemInline(admin.TabularInline):
    model = Imagem


class VariacaoInline(admin.TabularInline):
    model = Variacao
    min_num = 1
    extra = 0
    can_delete = True


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'tipo', 'descricao',
                    'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [
        VariacaoInline, ImagemInline
    ]

class ImagemAdmin(admin.ModelAdmin):
    list_display = ['produto', 'imagem']

class VariacaoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'nome', 'estoque']

class EntregaAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'usuario', 'status', 'cod_rastreamento']

class OTPAdmin(OTPAdminSite):
   pass


admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(Perfil_colaborador, PerfilAdmin)
admin_site.register(Endereco, EnderecoAdmin)
admin_site.register(Inf_bancarias, Inf_bancariasAdmin)
admin_site.register(Detalhe_cargo, Detalhe_cargoAdmin)
admin_site.register(Beneficios, BeneficiosAdmin)
admin_site.register(User)
admin_site.register(Group)
admin_site.register(Produto, ProdutoAdmin)
admin_site.register(Variacao,  VariacaoAdmin)
admin_site.register(Imagem, ImagemAdmin)
admin_site.register(Vaga)
admin_site.register(Perfil)
admin_site.register(Curriculo)
admin_site.register(Pedido)
admin_site.register(ItemPedido)
admin_site.register(Entrega, EntregaAdmin)
admin_site.register(Loja)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)


urlpatterns = [
    path('', include('produto.urls')),
    path('perfil/', include('perfil.urls')),
    path('pedido/', include('pedido.urls')),
    path('nossaslojas/', include('nossaloja.urls')),
    path('trabalheconosco/', include('trabalheconosco.urls')),
    path('pagar/PaymentController/', paymentController),
    path('pagar/', pagar),
    path('admin/', admin_site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
