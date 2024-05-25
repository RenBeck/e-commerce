from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.core.cache import cache
from . import models
from perfil.models import Perfil

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 20
    ordering = ['-id']


class Marketing(ListView):
    model = models.Produto
    template_name = 'produto/marketing.html'
    context_object_name = 'produtos'
    paginate_by = 20
    ordering = ['-id']


class Outlet(ListView):
    model = models.Produto
    template_name = 'produto/outlet.html'
    context_object_name = 'produtos'
    paginate_by = 20
    ordering = ['-id']


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imagens'] = models.Imagem.objects.filter(produto=self.object)
        return context
    

class Busca(ListaProdutos):
    def get_queryset(self, *args, **kwargs):
        termo = self.request.GET.get('termo') or self.request.session.get('termo', '')
        qs = super().get_queryset(*args, **kwargs)

        if not termo:
            return qs

        self.request.session['termo'] = termo

        qs = qs.filter(
            Q(nome__icontains=termo) |
            Q(descricao__icontains=termo)       
        )

        self.request.session.save()
        return qs
    
class CategoriaBusca(ListaProdutos):
    def get_queryset(self, *args, **kwargs):
        categoria = self.kwargs.get('categoria')
        qs = super().get_queryset(*args, **kwargs)

        if not categoria:
            return qs

        self.request.session['categoria'] = categoria

        qs = qs.filter(
            Q(categoria__in=[categoria])       
        )

        self.request.session.save()
        return qs
    

class SubCategoriaBusca(ListaProdutos):
    def get_queryset(self, *args, **kwargs):
        categoria = self.kwargs.get('categoria')
        sub_categoria = self.kwargs.get('subcategoria')
        qs = super().get_queryset(*args, **kwargs)

        if not categoria and sub_categoria:
            return qs

        self.request.session['categoria'] = categoria
        self.request.session['subcategoria'] = sub_categoria

        qs = qs.filter(
            Q (categoria__in=[categoria]) & Q(sub_categoria__in=[sub_categoria])         
        )

        self.request.session.save()
        return qs
    

class TipoBusca(ListaProdutos):
    def get_queryset(self, *args, **kwargs):
        categoria = self.kwargs.get('categoria')
        sub_categoria = self.kwargs.get('subcategoria')
        tipo = self.kwargs.get('tipo')
        qs = super().get_queryset(*args, **kwargs)

        if not categoria and sub_categoria:
            return qs

        self.request.session['categoria'] = categoria
        self.request.session['subcategoria'] = sub_categoria
        self.request.session['tipo'] = tipo

        qs = qs.filter(
            Q (categoria__in=[categoria]) & Q(sub_categoria__in=[sub_categoria]) & Q(tipo__in=[tipo])         
        )

        self.request.session.save()
        return qs


class AdicionarAosacola(View):
       def get(self, *args, **kwargs):

        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                self.request,
                'Produto não existe'
            )
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=variacao_id)
        variacao_estoque = variacao.estoque
        produto = variacao.produto

        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        preco_unitario = produto.preco
        preco_unitario_promocional = produto.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if imagem:
            imagem = imagem.name
        else:
            imagem = ''

        if variacao.estoque < 1:
            messages.error(
                self.request,
                'Estoque insuficiente'
            )
            return redirect(http_referer)

        if not self.request.session.get('sacola'):
            self.request.session['sacola'] = {}
            self.request.session.save()

        sacola = self.request.session['sacola']

        if variacao_id in sacola:
            quantidade_sacola = sacola[variacao_id]['quantidade']
            quantidade_sacola += 1

            if variacao_estoque < quantidade_sacola:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantidade_sacola}x no '
                    f'produto "{produto_nome}". Adicionamos {variacao_estoque}x '
                    f'no seu sacola.'
                )
                quantidade_sacola = variacao_estoque

            sacola[variacao_id]['quantidade'] = quantidade_sacola
            sacola[variacao_id]['preco_quantitativo'] = preco_unitario * \
                quantidade_sacola
            sacola[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * \
                quantidade_sacola
        else:
            sacola[variacao_id] = {
                'produto_id': produto_id,
                'produto_nome': produto_nome,
                'variacao_nome': variacao_nome,
                'variacao_id': variacao_id,
                'preco_unitario': preco_unitario,
                'preco_unitario_promocional': preco_unitario_promocional,
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocional': preco_unitario_promocional,
                'quantidade': 1,
                'slug': slug,
                'imagem': imagem,
            }

        self.request.session.save()
        

        messages.success(
            self.request,
            f'Produto {produto_nome} {variacao_nome} adicionado ao seu '
            f'sacola {sacola[variacao_id]["quantidade"]}x.'
        )

        return redirect(http_referer)


class RemoverDosacola(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            return redirect(http_referer)

        if not self.request.session.get('sacola'):
            return redirect(http_referer)

        if variacao_id not in self.request.session['sacola']:
            return redirect(http_referer)

        sacola = self.request.session['sacola'][variacao_id]

        messages.success(
            self.request,
            f'Produto {sacola["produto_nome"]} {sacola["variacao_nome"]} '
            f'removido do seu sacola.'
        )

        del self.request.session['sacola'][variacao_id]
        self.request.session.save()
        return redirect(http_referer)


class sacola(View):
    def get(self, *args, **kwargs):
        contexto = {
            'sacola': self.request.session.get('sacola', {})
        }

        return render(self.request, 'produto/sacola.html', contexto)



class ResumoDaCompra(View):
   def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            cache.set('direcionamento', 'sacola')
            return redirect('perfil:criar')

        perfil = Perfil.objects.filter(usuario=self.request.user).exists()

        if not perfil:
            messages.error(
                self.request,
                'Usuário sem perfil.'
            )
            return redirect('perfil:criar')

        if not self.request.session.get('sacola'):
            messages.error(
                self.request,
                'sacola vazio.'
            )
            return redirect('produto:lista')

        contexto = {
            'usuario': self.request.user,
            'sacola': self.request.session['sacola'],
        }
        cache.set('resumo_compra', 'resumodacompra')

        return render(self.request, 'produto/resumodacompra.html', contexto)

