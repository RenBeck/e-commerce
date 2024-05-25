from django.test import TestCase
from ..models import Loja

class Loja_test_models(TestCase):

    def  setUp(self):
        Loja.objects.create(
            loja= 'BS Savasse',
            rua="Rua dos Bobos",
            numero="1233",
            complemento="loja 303",
            bairro="Centro",
            cep="01234567",
            cidade="São Paulo",
            estado="SP"
        )

    def test_retorno(self):
        loja = Loja.objects.get(loja='BS Savasse')
        self.assertEqual(loja.loja, 'BS Savasse')
        self.assertEqual(loja.rua, "Rua dos Bobos")
        self.assertEqual(loja.numero, '1233')
        self.assertEqual(loja.complemento, 'loja 303')
        self.assertEqual(loja.bairro, 'Centro')
        self.assertEqual(loja.cep, '01234567')
        self.assertEqual(loja.cidade,'São Paulo')
        self.assertEqual(loja.estado, 'SP')