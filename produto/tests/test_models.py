from django.test import TestCase
from ..models import Produto, Variacao, Imagem

class Produto_test_models(TestCase):
    
    def setUp(self):

        produto = Produto.objects.create(
            nome ='Camisa',
            imagem = 'camisacinza.jpg',
            descricao = "Uma camisa preta",
            cor =  'Cinza',
            categoria = 'Masculino',
            sub_categoria = 'Roupa',
            tipo = 'Camisa',
            marca = 'Cocci',
            slug = 'camisa',
            preco = 50.90,
            preco_promocional =  45.90
        )

        Variacao.objects.create(
            produto = produto,
            nome = 'M',
            estoque = 11
        )

        Imagem.objects.create(
            produto = produto,
            imagem = 'camisa preta'
        )


    def test_retorno(self):
        produto = Produto.objects.get(nome='Camisa')
        self.assertEqual(produto.nome, 'Camisa')
        self.assertEqual(produto.imagem, 'camisacinza.jpg')
        self.assertEqual(produto.descricao, 'Uma camisa preta')
        self.assertEqual(produto.cor, 'Cinza')
        self.assertEqual(produto.categoria, 'Masculino')
        self.assertEqual(produto.sub_categoria, 'Roupa')
        self.assertEqual(produto.tipo, 'Camisa')
        self.assertEqual(produto.marca, 'Cocci')
        self.assertEqual(produto.slug, 'camisa')
        self.assertEqual(produto.preco, 50.90)
        self.assertEqual(produto.preco_promocional, 45.90)

        variacao = Variacao.objects.get(nome= 'M')
        self.assertEqual(variacao.nome, 'M')
        self.assertEqual(variacao.estoque, 11)

        imagem = Imagem.objects.get(imagem= 'camisa preta')
        self.assertEqual(imagem.imagem, 'camisa preta')
