from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib import messages
from django.core.cache import cache
from produto.models import Variacao
from .models import Pedido, ItemPedido
from utils import utils


class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')

        return super().dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(usuario=self.request.user)
        return qs


class Pagar(DispatchLoginRequiredMixin, DetailView):
    template_name = 'pedido/pagar.html'
    model = Pedido
    pk_url_kwarg = 'pk'
    context_object_name = 'pedido'


class SalvarPedido(View):
    template_name = 'pedido/pagar.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Você precisa fazer login.'
            )
            return redirect('perfil:criar')

        if not self.request.session.get('sacola'):
            messages.error(
                self.request,
                'Seu sacola está vazio.'
            )
            return redirect('produto:lista')

        sacola = self.request.session.get('sacola')
        sacola_variacao_ids = [v for v in sacola]
        bd_variacoes = list(
            Variacao.objects.select_related('produto')
            .filter(id__in=sacola_variacao_ids)
        )

        for variacao in bd_variacoes:
            vid = str(variacao.id)

            estoque = variacao.estoque
            qtd_sacola = sacola[vid]['quantidade']
            preco_unt = sacola[vid]['preco_unitario']
            preco_unt_promo = sacola[vid]['preco_unitario_promocional']

            error_msg_estoque = ''

            if estoque < qtd_sacola:
                sacola[vid]['quantidade'] = estoque
                sacola[vid]['preco_quantitativo'] = estoque * preco_unt
                sacola[vid]['preco_quantitativo_promocional'] = estoque * \
                    preco_unt_promo

                error_msg_estoque = 'Estoque insuficiente para alguns '\
                    'produtos do seu sacola. '\
                    'Reduzimos a quantidade desses produtos. Por favor, '\
                    'verifique quais produtos foram afetados a seguir.'

            if error_msg_estoque:
                messages.error(
                    self.request,
                    error_msg_estoque
                )

                self.request.session.save()
                return redirect('produto:sacola')

        qtd_total_sacola = utils.cart_total_qtd(sacola)
        valor_total_sacola = utils.cart_totals(sacola)

        pedido = Pedido(
            usuario=self.request.user,
            total=valor_total_sacola,
            qtd_total=qtd_total_sacola,
            status='Criado',
        )

        pedido.save()
        cache.set('pedido_id', pedido.pk)
        cache.set('user', pedido.usuario)

        ItemPedido.objects.bulk_create(
            [
                ItemPedido(
                    pedido=pedido,
                    produto=v['produto_nome'],
                    produto_id=v['produto_id'],
                    variacao=v['variacao_nome'],
                    variacao_id=v['variacao_id'],
                    preco=v['preco_quantitativo'],
                    preco_promocional=v['preco_quantitativo_promocional'],
                    quantidade=v['quantidade'],
                    imagem=v['imagem'],
                ) for v in sacola.values()
            ]
        )

        del self.request.session['sacola']

        return redirect(
            reverse(
                'pedido:pagar',
                kwargs={
                    'pk': pedido.pk
                }
            )
        )


class Detalhe(DispatchLoginRequiredMixin, DetailView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'pedido/detalhe.html'
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        cache.set('pedido_id', obj.pk)  
        return obj


class Lista(DispatchLoginRequiredMixin, ListView):
    model = Pedido
    context_object_name = 'pedidos'
    template_name = 'pedido/lista.html'
    paginate_by = 10
    ordering = ['-id']
