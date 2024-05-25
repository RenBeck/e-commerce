from django.test import TestCase
from ..models import Produto
from django.urls import reverse


class Produto_Wiew_Test(TestCase):

    def setUp(self):

        Produto.objects.create(
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

    def test_status_core_200_marketing(self):
        response = self.client.get(reverse('produto:marketing'))
        self.assertEqual(response.status_code, 200)

    def test_status_core_200_lista(self):
        response = self.client.get(reverse('produto:lista'))
        self.assertEqual(response.status_code, 200)

    def test_status_core_200_detalhe(self):
        response = self.client.get(reverse('produto:detalhe', kwargs={'slug': 'camisa'}))
        self.assertEqual(response.status_code, 200) 

    def test_status_core_200_adicionaraosacola(self):
        response = self.client.get(reverse('produto:adicionaraosacola'))
        self.assertEqual(response.status_code, 302)
        redirected_response = self.client.get(response.url)
        self.assertEqual(redirected_response.status_code, 200)

    def test_status_core_200_removerdosacola(self):
        response = self.client.get(reverse('produto:removerdosacola'))
        self.assertEqual(response.status_code, 302)
        redirected_response = self.client.get(response.url)
        self.assertEqual(redirected_response.status_code, 200)

    def test_status_core_200_sacola(self):
        response = self.client.get(reverse('produto:sacola'))
        self.assertEqual(response.status_code, 200)

    def test_status_core_200_resumodacompra(self):
        response = self.client.get(reverse('produto:resumodacompra'))
        self.assertEqual(response.status_code, 302)
        redirected_response = self.client.get(response.url)
        self.assertEqual(redirected_response.status_code, 200)

    def test_status_core_200_busca(self):
        self.client.session['termo'] = "camisa"
        self.client.session.save()

        response = self.client.get(reverse('produto:busca'))
        self.assertEqual(response.status_code, 200)

    def test_status_core_200_busa_categoria(self):
        response = self.client.get(reverse('produto:buscacategoria', kwargs={'categoria': 'Masculino'}))
        self.assertEqual(response.status_code, 200) 

    def test_status_core_200_busca_subCategoria(self):
        response = self.client.get(reverse('produto:buscasubcategoria', kwargs={'categoria': 'Masculino', 'subcategoria':'Roupa'}))
        self.assertEqual(response.status_code, 200) 

    def test_status_core_200_busca_tipo(self):
        response = self.client.get(reverse('produto:buscatipo', kwargs={'categoria':'Masculino', 'subcategoria':'Roupa', 'tipo':'Camisa'}))
        self.assertEqual(response.status_code, 200) 

    def test_status_core_200_outlet(self):
        response = self.client.get(reverse('produto:outlet'))
        self.assertEqual(response.status_code, 200)
        