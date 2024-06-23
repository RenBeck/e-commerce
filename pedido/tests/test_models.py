from django.test import TestCase
from ..models import Pedido, ItemPedido

from django.contrib.auth.models import User

class Pedido_test_models(TestCase):

    def setUp(self):
        user = User.objects.create(username="Beck")

        pedido = Pedido.objects.create(
            usuario=user,
            total= 400.98,
            qtd_total= 7,
            status= 'Criado'
        )

        ItemPedido.objects.create(
            pedido=pedido,
            produto='Camiseta',
            produto_id=1,
            variacao='M',
            variacao_id=1,
            preco=100.98,
            preco_promocional=90.98,
            quantidade=3,
            imagem='camiseta azul',
            devolvido=False
        )


    def test_retorno(self):

        user = User.objects.get(username="Beck")

        pedido = Pedido.objects.get(usuario=user)
        self.assertEqual(pedido.usuario, user)
        self.assertEqual(pedido.total, 400.98)
        self.assertEqual(pedido.qtd_total, 7)
        self.assertEqual(pedido.status, 'Criado')

        item_pedido = ItemPedido.objects.get(pedido=pedido)
        self.assertEqual(item_pedido.pedido, pedido)
        self.assertEqual(item_pedido.produto, 'Camiseta')
        self.assertEqual(item_pedido.produto_id, 1)
        self.assertEqual(item_pedido.variacao, 'M')
        self.assertEqual(item_pedido.variacao_id, 1)
        self.assertEqual(item_pedido.preco, 100.98)
        self.assertEqual(item_pedido.preco_promocional, 90.98)
        self.assertEqual(item_pedido.quantidade, 3)
        self.assertEqual(item_pedido.imagem, 'camiseta azul')
        
